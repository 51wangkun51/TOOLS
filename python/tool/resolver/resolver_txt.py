import os,sys
class Rel_Txt():
    def __init__(self,filepath):

        self.sshconfig = filepath

    def readtxt(self):
        config={}
        try :
            fo = open(self.sshconfig,"r")
            for line in fo.readlines():
                line=line.strip()
                tmp=line.split("=")
                config[tmp[0]]=tmp[1]
        except Exception as e :
            print("文件打开失败")
            sys.exit(-1)
        finally:
            if "fo" in locals() or "fo" in globals() :
                fo.close()
        print(config)
        return config
    def splitdic(self):
        self.config1 = self.readtxt()
        #num = self.config.__len__()
        configkeys = list(self.config1.keys())
        configlist = []
        for k in range(configkeys.__len__()//4):
            print("第",k+1,"组配置")
            n = 0
            tmpdic1 = {}
            for i in configkeys[k * 4:] :
                print( i ,"=",self.config1[i])
                tmpdic1[i] = self.config1[i]
                n +=1
                if n == 4 :
                    break
            configlist.append(tmpdic1)
        return configlist


currentpath = os.path.dirname(os.path.realpath(__file__))
filename = "ssh.txt"
sshconfig = currentpath+"/"+filename
rel = Rel_Txt(sshconfig)
configlist = rel.splitdic()
print(configlist)
print(configlist.__len__())