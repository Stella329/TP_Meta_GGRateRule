# Source chatgpt
# 如果你的 XML 结构包含更多层级，你可以使用递归来遍历所有嵌套层，同时保留层级路径

import xml.etree.ElementTree as ET
import pandas as pd

# 示例 XML 数据
xml_data = ''' 
<raterulecondition>
    <RateRule id="More Layer">
        <UserRateCondition>
            <layer1>
                <layer2>
                    <layer3>
                        <layer4>layer4 content</layer4>
                    </layer3>
                </layer2>
            </layer1>
        </UserRateCondition>

        <UserRateCondition op="none">
            <LanguageCode>th</LanguageCode>
        </UserRateCondition>
    </RateRule>
</raterulecondition>
'''

# 解析 XML
root = ET.fromstring(xml_data)


def parse_element(element, parent_key=""):
    """
    递归解析 XML 节点，并返回所有层级的文本内容和属性。
    """
    data = {}

    # 生成当前层的 Key（层级路径）
    key = f"{parent_key}.{element.tag}" if parent_key else element.tag

    # 获取文本内容（去掉多余空格）
    if element.text and element.text.strip():
        data[key] = element.text.strip()

    # 解析属性
    for attr, value in element.attrib.items():
        data[f"{key}@{attr}"] = value

    # 递归解析子元素
    for child in element:
        child_data = parse_element(child, key)
        data.update(child_data)

    return data


# 遍历所有顶级子元素（支持多个 RateRule）
parsed_data = [parse_element(rate_rule) for rate_rule in root]

# 创建 DataFrame
df = pd.DataFrame(parsed_data)

# 保存到 Excel
df.to_excel("parsed_xml.xlsx", index=False)

print("XML 数据已成功解析并保存到 Excel。")
