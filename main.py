import xml.etree.ElementTree as ET
import categorizer
import format

# 读取
fileName = 'Ctrip - Rate Rules0903.xml'
tree = ET.parse(fileName)
root = tree.getroot()


#新建最高层root
root_sing = ET.Element('RateRuleSettings_sing')
root_EN = ET.Element('RateRuleSettings_EN')
root_multi = ET.Element('RateRuleSettings_multi')


##内容库：唯一list[{1},{2}...]
categ = categorizer.Categorizer(fileName)
all_ids = categ.infoCollection
# print(len(all_ids))
# # print(all_ids)
# categ.checker()




#ID库
id_LANG_EN = categ.id_LANG_EN
idMulLang = categ.idMulLang
idSLang = categ.idSLang
id_Q = categ.id_Q
id_M = categ.id_M
id_Q_M = categ.id_Q_M

for item in all_ids:
    # print(f'item = {item}') ##测试
    idName=item['id']
    country = item['country']
    langCode =item['languageCode']


    # ## LANG_单语言
    # if idName in idSLang:
    #     xml_sing = Format.XmlFormat(idName, country, langCode) ##obj.
    #     xml_sing.set_rule_SingLang() ##单语言规则写入
    #     root_sing.append(xml_sing.root) ##规则加入the root


    ## LANG_EN
    if idName in id_LANG_EN:
        xml_en = Format.XmlFormat(idName, country, langCode)
        xml_en.set_rule_EN()
        root_EN.append(xml_en.root)


# xml_sing.write_xml(xml_name='lang_singular_M_Q', root=root_sing)
# print( f'\n单语言最终条目数量 = {len(root_sing)}')

xml_en.write_xml(xml_name='lang_EN_M_Q', root=root_EN)
print( f'\nEN-XX最终条目数量 = {len(root_EN)}')





