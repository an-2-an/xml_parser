import xml.etree.ElementTree as ET
tree = ET.parse('my.xml')
root = tree.getroot()

#main tag
print(root.tag)
print('-' * 20)

#sub tags
for child in root:
    print(child.tag, child.attrib)
    for c in child:
        print(c.tag, c.attrib, c.text)
    print('-------')

print('-' * 20)

#countries names and years
for child in root:
    name = child.get('name')
    year = int(child.find('year').text)
    print(name, year)


'''
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
'''

