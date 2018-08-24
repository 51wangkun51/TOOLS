import os,sys
import xml.etree.cElementTree as ET
class Rel_Xml() :
    def __init__(self,path):
        self.filename = path
    def readxml(self):
        config = {}
        configlist = []
        try:
            print(os.path.exists(filename))
            tree = ET.parse(self.filename)
            print("tree :",type(tree))
            root = tree.getroot()
            print("root :",type(root))
            print("root attribute" , root.attrib)
            propertys = root.findall("property")
            print(type(propertys))
            for p in propertys :
                for child in p :
                    config[child.tag] = child.text
                configlist.append(config)


        except Exception as e :
            print(e)
        print(configlist)
        return configlist
    def splitdic(self):
        configlist = []
        config = self.readxml()


        return configlist





currentpath = os.path.dirname(os.path.realpath(__file__))
filename = "ssh.xml"
sshconfig = currentpath+"/"+filename
relx = Rel_Xml(sshconfig)
configlist = relx.splitdic()
# print(configlist[2])
# print(configlist.__len__())