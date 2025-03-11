# From chatgpt:
# 在Python代码中处理XML中的嵌套标签，你可以修改遍历XML树的方式，以便能够记录每个元素的层级关系。以下是一个更新后的脚本，它可以处理嵌套标签，并将它们以层级结构存储在Excel中

import xml.etree.ElementTree as ET
import pandas as pd

# 解析 XML
xml_data = '''
<Root>
 <RateRule id="LANG_TH_Q">
  <Description>Member - For Thailand</Description>
  <UserRateCondition op="all">
   <UserRateCondition reference_id="17"/>
   <LanguageCode>th</LanguageCode>
  </UserRateCondition>
 </RateRule>
 <RateRule id="LANG_TH_EN_Q">
  <Description>Member - For Thailand_EN</Description>
  <UserRateCondition op="all">
   <UserRateCondition>
    <UserRateCondition reference_id="17"/>
   </UserRateCondition>
   <UserRateCondition op="none">
    <LanguageCode>th</LanguageCode>
   </UserRateCondition>
  </UserRateCondition>
 </RateRule>
</Root>
'''

root = ET.fromstring(xml_data)


def parse_element(element, parent_key=""):
    data = {}
    for child in element:
        key = f"{parent_key}.{child.tag}" if parent_key else child.tag

        if child.text and child.text.strip():
            data[key] = child.text.strip()

        if child.attrib:
            for attr, value in child.attrib.items():
                data[f"{key}@{attr}"] = value

        child_data = parse_element(child, key)
        data.update(child_data)

    return data


# 解析 XML 数据
parsed_data = [parse_element(rate_rule) for rate_rule in root]

# 创建 DataFrame
df = pd.DataFrame(parsed_data)

# 保存到 Excel
df.to_excel("parsed_xml.xlsx", index=False)

print("XML 数据已成功解析并保存到 Excel。")
