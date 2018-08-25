import os,sys

class Rel_Excel() :
    def __init__(self,path):
        self.file = path
    def readxml(self):
        pass
    def splitdic(self):
        pass



currentpath = os.path.dirname(os.path.realpath(__file__))
filename = "ssh.xml"
sshconfig = currentpath+"/"+filename
rele = Rel_Excel(sshconfig)
configlist = rele.splitdic()
print(configlist[2])
print(configlist.__len__())