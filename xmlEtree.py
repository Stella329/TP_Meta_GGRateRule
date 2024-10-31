import xml.etree.ElementTree as ET
import dataCleaner
import Format

# # 读取
# fileName = 'Ctrip - Rate Rules0903.xml'
# tree = ET.parse(fileName)
# root = tree.getroot()
#
#
# # 读取tag和attribute
# for child in root:  ##root具有标签和属性字典。-- UserRateCondition {'id': '10', 'op': 'all'}..., RateRule {'id': 'LANG_GR_Q'}...
#     print(child.tag)
#     print(child.attrib)
#
# print(root[1][0].text) ##子集嵌套：通过索引访问特定的子级节点（不含注释） --return MY
#
# 查找：for
#
# #Element.iter('tag'): 创建一个以当前元素为根元素的树的 iterator
#
# for item in root.iter('RateRule'):
#     print(item.attrib) ##返回所有已创建raterule tag中的element's attri：原文：<RateRule id="LANG_EN">...；返回：-- {'id': 'LANG_EN'}，{'id': 'LANG_JP'} {'id': 'LANG_HK'} {'id': 'LANG_HK_EN'}...
#
#
# Element.findall() 仅查找当前element的 直接子元素中，带有指定 标签内容 的元素。
# Element.find() 找带有特定标签的 第一个 子级，然后可以用 Element.text 访问元素的文本内容。
# Element.get 访问element的attri
# for item in root.findall('RateRule'):
#     print(item.attrib) ##返回结果=同上，root.iter('RateRule')


#————————————————————————————————————————————————

file = Categorizer.Categorizer(fileName)
file.infoCollector()

idMulLang_list = file.idMulLang
idSLang_list = file.idSLang
id_Q_list = file.id_Q
id_M_list = file.id_M
id_Q_M_list = file.id_Q_M


#新建单语言站点规则：
for item in idSLang_list:
    idName = item['id']
    langCode = item['languageCode']
    country = item['country'] ## <class 'list'>
    length = len(country)

    # print(f'country={country}') ##检查用
    # print(f'length={length}')

    format = xmlFormat.XmlFormat(idName, country, langCode, length)


    if item['id'] != 'LANG_EN':
        single = format.sLang()
        for line in single:
            print(line)

    else:
        # print('id=LANG_EN') ##检查用
        LANG_EN_Q_M = format.ruleForLANG_EN()
        for line in LANG_EN_Q_M:
            print(line)


#检查用：
print('\n以下是检查结果：统计')
print(f'idSLang_list={idSLang_list}, \ncount={len(idSLang_list)}')
print(f'\nidMulLang_list={idMulLang_list}, \ncount={len(idMulLang_list)}')
print(f'\nid_Q_list={id_Q_list}, \ncount={len(id_Q_list)}')
print(f'\nid_M_list={id_M_list}, \ncount={len(id_M_list)}')
print(f'\nid_Q_M_list ={id_Q_M_list }, \ncount={len(id_Q_M_list)}')
