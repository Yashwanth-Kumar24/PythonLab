import xml.etree.ElementTree as ET
mytree = ET.parse('details.xml')
myroot = mytree.getroot()

for child in myroot:
    if(child.tag=="Student"):
        b=input("Enter new branch for "+child.find('Name').text)
        child.find('Branch').text = str(b)
        child.find('Branch').set('Updated','yes')

mytree.write('editedDetails.xml')
