# Source ima: 这个脚本假设XML结构是扁平的，即没有嵌套的相同标签。如果XML结构更复杂，需要用嵌套轮询

# 安装：pandas使用openpyxl来写入Excel文件
# pip install pandas openpyxl

import xml.etree.ElementTree as ET
import pandas as pd

# 待解析的XML字符串
xml_data = '''
<RateRule id="LANG_JP_Q_T">
    <Description>Member - For JP- Userlist</Description>
    <UserRateCondition>
        <UserListId>8915055875</UserListId>
    </UserRateCondition>
</RateRule>
'''

# 解析XML
root = ET.fromstring(xml_data)

# 创建一个空字典来存储数据
data = {}

# 遍历XML树，提取标签和文本内容
for elem in root.iter():
    # 获取当前元素的标签名
    tag = elem.tag
    # 获取当前元素的文本内容，如果有的话
    text = elem.text.strip() if elem.text else ''
    # 将标签和文本内容存储到字典中
    data[tag] = text

# 将字典转换为DataFrame
df = pd.DataFrame([data])

# 将DataFrame保存到Excel文件
excel_file = 'output.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data has been written to {excel_file}")
