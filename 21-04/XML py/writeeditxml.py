import xml.etree.ElementTree as ET
mytree = ET.parse('details.xml')
myroot = mytree.getroot()

for i in range(len(myroot)):
    ET.SubElement(myroot[i],'specialization')

k=0
for i in myroot.iter('specialization'):
    sp=input('Enter specialization for '+myroot[k].find("Name").text)
    i.text=sp
    k+=1

mytree.write('newAttributeAdd.xml')
