from varname import nameof
import xml.etree.ElementTree as ET 

user = {
    'name': 'Eduardo Ismael',
    'age': 27,
    'books': [
        {
            'title' : 'Carry',
            'author': 'stephen king'
        },
        {
            'title': 'Choque de reyes',
            'author': 'Gorge R. R. Martin'
        }
    ]
}

def JSONToXML(var, var_name):
    root = ET.Element(var_name)
    for key in var.keys():
        ET.SubElement(root, key).text = str(var[key])
    tree = ET.ElementTree(root)
    tree.write("../resources/{}.xml".format(var_name))
        
JSONToXML(user, nameof(user))