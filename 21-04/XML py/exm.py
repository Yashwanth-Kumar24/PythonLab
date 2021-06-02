import xml.etree.ElementTree as ET
mytree = ET.parse('details.xml')
myroot = mytree.getroot()

for i in myroot.iter('Name'):  ## reaading name tags
    print(i.text)

for child in myroot:  #reading specific tag-subtags
    if(child.tag=="Student"):
        print(child.find('Branch').text)

#writing in xml
for i in range(len(myroot)):
    ET.SubElement(myroot[i],'specialization')


for i in myroot.iter('specialization'):
    sp=input('Enter specialization')
    i.text=sp
    

mytree.write('newAttributeAdd.xml')

mytree.write("Edited.xml")


