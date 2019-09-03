from dicttoxml import dicttoxml
import xml.dom.minidom as md

dictionary = {
        'head': {"title": "XML"},

        'body': {"h1": "This is title", 'h2': 'This is H2!'}
}


ugly_xml = dicttoxml(dictionary, custom_root='html', attr_type=False)
xml_str = ugly_xml.decode('utf-8')
print(xml_str)

# https://www.freeformatter.com/xml-formatter.html

xml = md.parseString(xml_str)
xml_pretty = xml.toprettyxml()
print(xml_pretty)

with open('my1.html', 'w') as f:
    f.write(xml_pretty)
