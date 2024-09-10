import xml.etree.ElementTree as ET

class Categorizer:
    '''what：数据清洗 + 数据汇总（创建一个唯一all_id库）'''
    def __init__(self, fileName):
        self.fileName = fileName
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

        self.infoCollection = []  ##--[{'id': 'LANG_NL', 'description': 'For The Netherlands', 'country': ['NL'], 'languageCode': []}, {'id': 'LANG_PL', ...}]
        self.infoCollector()

        self.info_dict ={}

        self.id_LANG_EN = []
        self.idMulLang = []
        self.idSLang = []
        self.id_Q = []
        self.id_M = []
        self.id_Q_M = []
        self.idCategorizer()

    def infoCollector(self):
        '''收集所有信息,于一个dictionary中：key = Raterule ID; value =该ID下的所有信息, 包括description, country, languageCode'''
        for item in self.root.findall('RateRule'):

            container = {} ##容器

            ##第一层
            id = item.attrib['id']  ##raterule tag中的id -- Return dic: {'id': 'LANG_EN'}
            description = item.find('Description').text  ##-- string

            container['id'] = id
            container['description'] = description


            ##第二层: under <UserRateCondition>
            for child in item:  ##遍历第二层的节点和标签名和属性: <UserRateCondition op="all">下

                ##国家：<UserCoutnry>有的在二层，有的在三层
                country_list = []
                for country in child.iter('UserCountry'):
                    country_list.append(country.text)
                container['country'] = country_list

                ##语言：languageCode存在于多语言情况
                language_list =[]
                for type in child.iter('LanguageCode'):
                    language_list.append(type.text)

                container['languageCode'] = language_list


                # ## tag1: <UserRateCondition op="all">
                # userRateCondition_1 = item.find('UserRateCondition').attrib
                # try:
                #     op = userRateCondition_1['op']
                # except KeyError:  ##返回空值{}
                #     op = 0
                # container['userRateCondition_1'] = op

            self.infoCollection.append(container)
        return self.infoCollection


    def idCategorizer(self):
        '''作用：给ID分组
        后续逻辑：ID分完组，用ID name在infocollector中轮询'''
        for subject in self.infoCollection:
            idName = subject['id']

            if idName == 'LANG_EN':
                self.id_LANG_EN.append(idName)

            elif '_Q_M' in idName:
                self.id_Q_M.append(idName)

            elif idName[-2:]=='_M': ##避免有LANG_MY类似混入; 已排除’_Q_M‘
                self.id_M.append(idName)

            elif '_Q' in idName:
                self.id_Q.append(idName)

            elif len(idName) < 8 and subject['languageCode']==[]:  ##regular prices
                self.idSLang.append(idName)

            else:
                self.idMulLang.append(idName)


    def checker(self):
        '''检查用'''
        print('\n以下是检查结果：统计')
        print(f'\nidLANG_EN={self.id_LANG_EN}, \ncount={len(self.id_LANG_EN)}')
        print(f'\nidSLang_list={self.idSLang}, \ncount={len(self.idSLang)}')
        print(f'\nidMulLang_list={self.idMulLang}, \ncount={len(self.idMulLang)}')
        print(f'\nid_Q_list={self.id_Q}, \ncount={len(self.id_Q)}')
        print(f'\nid_M_list={self.id_M}, \ncount={len(self.id_M)}')
        print(f'\nid_Q_M_list ={self.id_Q_M}, \ncount={len(self.id_Q_M)}')


