#生成XML文件模板页
import xml.etree.ElementTree as ET

class XmlFormat:
    '''what：xml模板样式（不同语言）
    建议：分别创建不同的xml object'''
    def __init__(self,idName, country, langCode):
        self.idName=idName
        self.country = country  ##list
        self.langCode = langCode ##list
        self.root = ET.Element('RateRule')
        self.root.set('id',f'{self.idName}')  ## --{'id': 'LANG_EN'}


    def setRule_EN_QM(self): ##EN_Q_M
        '''创建单条child'''
        self.root.set('id', f'{self.idName}_Q_M')
        child1=ET.SubElement(self.root, 'Description') ##child1 = ET.SubElement(root, "child1")
        child1.text = f'Mobile Membership - {str(self.idName[5:])}'
        child2=ET.SubElement(self.root, 'UserRateCondition')
        child2.set('op', "all") ##__child2.set(__key, __value)

        grandchild1=ET.SubElement(child2, 'UserDeviceType')  #M
        grandchild1.text = 'Mobile'
        grandchild2 = ET.SubElement(child2, 'UserSignedIn')  #Q
        grandchild2.text = 'true'

        child3=ET.SubElement(self.root, 'UserRateCondition') #EN-XX: 排除已有站点的countries
        child3.set('op', 'none')

        # print(f'检查用country={self.country}') ##test
        for c in self.country:
            grandchild3 = ET.Element('UserCountry')
            grandchild3.text = c
            child3.append(grandchild3)



    def setRule_sing_QM(self): ##单语言_Q_M
        '''创建单条child'''
        self.root.set('id', f'{self.idName}_Q_M')
        child1=ET.SubElement(self.root, 'Description')
        child1.text = f'Mobile Membership - {str(self.idName[5:])}'
        child2=ET.SubElement(self.root,'UserRateCondition')
        child2.set('op', "all")


        grandchild1=ET.SubElement(child2, 'UserDeviceType') #M
        grandchild1.text = 'Mobile'
        grandchild2 = ET.SubElement(child2, 'UserSignedIn')  #Q
        grandchild2.text = 'true'

        num=3
        for i in range(0,len(self.country)): #如果多Country
            globals()[f'grandchild{num+i}'] = ET.SubElement(child2, 'UserCountry')  ## grandchild3, 4, 5...
            globals()[f'grandchild{num+i}'].text = self.country[i]  ## grandchild3.text



    # TODO def setRule_mulMother(self): ##多语言-本国语
    # TODO def setRule_mulEN(self): ##多语言-英语




    def write_xml(self, xml_name, root):
        '''写入XML文件;
        root: main.py中更高一层，由外部输入
        tree.write()方法接受一个文件对象，一个可选的编码参数（默认为'utf-8'），以及一个布尔值xml_declaration，它决定是否应该在文件的开头写入XML声明（<?xml version="1.0" encoding="UTF-8"?>）
        '''
        tree = ET.ElementTree(root)

        with open(f"{xml_name}.xml", "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)





