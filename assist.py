# # # 模板制作：复制粘贴
# # # list.append("
# # # ")
# #
# # list = []
# # list.append("<RateRule id='LANG_HK_M_Q'>")
# # list.append("<Description>Mobile Membership - For HK </Description>")
# #
# # list.append("<UserRateCondition op='all'>")
# # list.append("<UserDeviceType>mobile</UserDeviceType>")
# # list.append("<UserSignedIn>true</UserSignedIn>")
# # list.append("<LanguageCode>zh-tw</LanguageCode>")
# # list.append("<UserRateCondition reference_id='111' />")
# # list.append("</UserRateCondition>")
# #
# # list.append("</RateRule>")
# #
# # print(list)
# #
# # for item in list:
# #     print("f"+"'"+f"{item}"+"'")
#
#
#
# id_dic={}
#
# # 测试
# import xml.etree.ElementTree as ET
#
# # 读取
# tree = ET.parse('Ctrip - Rate Rules0903.xml')
# root = tree.getroot()
#
#
# for item in root.findall('RateRule'):
#     id = item.attrib ##raterule tag中的id -- Return dic: {'id': 'LANG_EN'}
#
#     for child in item: ##遍历第二层的节点和标签名和属性
#         try:
#             country = child.findall('UserCountry')
#         except AttributeError:
#             country = 0
#             id_dic['country'] = country
#         else:
#             step=0
#             for region in country:
#                 id_dic[f'country{step}']=region
#                 step+=1
# print(id_dic)
#

id = 'LANG_IN_M'
print(id[-2:])
