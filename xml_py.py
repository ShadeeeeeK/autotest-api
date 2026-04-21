import xml.etree.ElementTree as ET

xml_data = """
<note>
    <to>Sergey</to>
    <from>ChatGPT</from>
    <message>Привет, это простой XML</message>
</note>
"""

root = ET.fromstring(xml_data)

print(root.find('to').text)

