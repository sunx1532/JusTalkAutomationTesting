import xml.dom.minidom as DOM

device_tree = DOM.parse("../../Config/Deviceinfo.xml")

collections = device_tree.documentElement

collections



print(collections)
