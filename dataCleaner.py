import xml.etree.ElementTree as ET

class Categorizer:
    '''what：数据清洗 + 数据汇总（创建一个唯一all_id库）'''
    def __init__(self, fileName):
        self.fileName = fileName
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

        self.infoCollection = []  ##含所有信息--[{'id': 'LANG_NL', 'description': 'For The Netherlands', 'country': ['NL'], 'languageCode': []}, {'id': 'LANG_PL', ...}]
        self.collect_info() ##method, 添加所有信息

        self.info_dict ={}
        ## ID库：将ID分类
        self.id_LANG_EN = []
        self.idMulLang = []
        self.idSLang = []
        self.id_Q = []
        self.id_M = []
        self.id_Q_M = []
        self.idCategorizer()

    def collect_info(self):
        '''1. 轮询xml，收集每条信息放入containner(dictionary)中：key = Raterule ID; value =该ID下的所有信息, 包括description, country, languageCode
        2. container放入infoCollector中（list)'''
        for item in self.root.findall('RateRule'):

            container = {} ##新建容器：key=value名称，value=value值

            ##第一层：<RateRule id="LANG_XX">下
            id = item.attrib['id']  ##raterule tag中的id -- Return dic: {'id': 'LANG_EN'}
            description = item.find('Description').text  ##-- string

            container['id'] = id
            container['description'] = description


            ##第二层: <UserRateCondition>下
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


                # ## 收录第二层的attribute
                # ## 0=不适用
                # layer2_attrib = item.find('UserRateCondition').attrib
                # try:
                #     op = layer2_attrib['op']
                # except KeyError:  ##返回空值{}
                #     op = 0
                # container['layer2_attrib'] = op
                #
                #
                # ##第三层：more <UserRateCondition>
                # ## 多语言：内容混乱，且有引入op="none/all"区分国家；reference_id="xx"关联前序ref_id；需单独拆分
                # ## 0=不适用
                # try:
                #     for grandchild in child.findall('UserRateCondition'):
                #         pass



            self.infoCollection.append(container)
        return self.infoCollection



    # TODO def collect_info2(self):
    #     """【优先级低】：collect_info2方法升级版：用Etree轮询，而不用一层一层筛选"""


    def idCategorizer(self):
        '''作用：按照ID的名称，区分多语言、单语言和M,Q等价格'''
        for item in self.infoCollection:
            id_name = item['id']

            if id_name == 'LANG_EN':
                self.id_LANG_EN.append(id_name)

            elif '_Q_M' in id_name:
                self.id_Q_M.append(id_name)

            elif id_name[-2:]=='_M': ##排除: 1. 避免LANG_MY类似混入(必须以_M结尾）; 2.排除’_Q_M‘
                ## 截取逻辑：'LANG_MY_M'[-1:] == M; 'LANG_MY_M'[-2:] == _M
                self.id_M.append(id_name)

            elif '_Q' in id_name:
                self.id_Q.append(id_name)

            elif len(id_name) < 8 and item['languageCode']==[]:  ##单语言站点：1.string长度 2. 无language code
                self.idSLang.append(id_name)

            else:
                self.idMulLang.append(id_name)


    def checker(self):
        '''检查用'''
        print('\n以下是检查结果：统计')
        print(f'\nidLANG_EN={self.id_LANG_EN}, \ncount={len(self.id_LANG_EN)}')
        print(f'\nidSLang_list={self.idSLang}, \ncount={len(self.idSLang)}')
        print(f'\nidMulLang_list={self.idMulLang}, \ncount={len(self.idMulLang)}')
        print(f'\nid_Q_list={self.id_Q}, \ncount={len(self.id_Q)}')
        print(f'\nid_M_list={self.id_M}, \ncount={len(self.id_M)}')
        print(f'\nid_Q_M_list ={self.id_Q_M}, \ncount={len(self.id_Q_M)}')


