import os,sys
currentpath = os.path.dirname(os.path.realpath(__file__))
filename = "ssh.txt"
sshconfig = currentpath+"/"+filename
config={}
try :
    fo = open(sshconfig,"r")
    for line in fo.readlines():
        print("111",line)
        line.replace("\n","")
        print("222",line)
        tmp=line.split("=")
        config[tmp[0]]=tmp[1]
        print(tmp)
except Exception as e :
    print("文件打开失败")
    sys.exit(-1)
finally:
    if "fo" in locals() or "fo" in globals() :
        fo.close()
print(config)