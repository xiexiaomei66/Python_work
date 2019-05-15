from xml.dom import minidom
dom=minidom.parse('Class_info.xml')

root=dom._get_documentElement()

names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
cities=root.getElementsByTagName('city')

for i in range(0,4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(cities[i].firstChild.data)