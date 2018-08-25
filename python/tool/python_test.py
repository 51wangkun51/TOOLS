# print("读取命令行")
# str1 = input("请输入")
# print(str1)
'''--------------------------------------------------------------------------------------------------------------------------------'''
# print("获取当前路径和时间")
# import os,sys
# print(sys.path[0]) #脚本当前路径
# print(sys.argv[0]) #脚本当前路径带脚本名 first
# print(os.getcwd()) #执行路径，如果你在C:\test目录下执行python getpath\getpath.py，那么os.getcwd()会输出“C:\test”，sys.path[0]会输出“C:\test\getpath”
# print(os.path.realpath(__file__)) # 获取当前文件__file__的路径 first
# print(os.path.dirname(os.path.realpath(__file__))) # 获取当前文件__file__的所在目录
# print( os.path.split(os.path.realpath(__file__))[0]) # 获取当前文件__file__的所在目录
# '''
# D:\>python ./python_test/test_path.py
# os.getcwd() “D:\”，取的是起始执行目录
# sys.path[0]或sys.argv[0] “D:\python_test”，取的是被初始执行的脚本的所在目录
# os.path.split(os.path.realpath(__file__))[0] “D:\python_test”，取的是__file__所在文件test_path.py的所在目录'''
#
# import datetime
# nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
# pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
# afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
# tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
# print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
'''--------------------------------------------------------------------------------------------------------------------------------'''
# print("判断文件/文件夹是否存在")
# import os
#print(os.path.exists("F:/project/python/tool/resolver/ssh.txt"))
# print(os.path.exists("F:\\project\\python\\tool/resolver\\ssh.txt"))
# try :
#     fo = open("F:/project/python/tool/resolver/ssh1.txt","r")
# except Exception as e :
#     print("异常")
# finally:
#     if "fo" in locals() or "fo" in globals():
#         print("存在",fo)
#         fo.close()
#     else:
#         print("不存在","fo")
'''--------------------------------------------------------------------------------------------------------------------------------'''
#print("判断文件是否可做读写操作")
# os.F_OK: 检查文件是否存在;
# os.R_OK: 检查文件是否可读;
# os.W_OK: 检查文件是否可以写入;
# os.X_OK: 检查文件是否可以执行
# import os
# file = "F:\\project\\python\\tool/resolver\\ssh.txt"
# print(os.access(file,os.F_OK))
# print(os.access(file,os.R_OK))
# print(os.access(file,os.W_OK))
# print(os.access(file,os.X_OK))
'''--------------------------------------------------------------------------------------------------------------------------------'''
#print("读取文件")
# with open("demo.txt", "r") as f:
#     data = f.readlines()
#     print(data)
#     print(type(data))
'''--------------------------------------------------------------------------------------------------------------------------------'''
#print("打印字典")
dic1 = {'name ': ' wangkun', 'ip ': ' 10.11.12.13', 'port ': ' 22', 'password ': ' Changeme_123'}
# for k,v in dic1.items() :
#     print("k = %s , v = %s" % (k , v))
#
# for k in dic1 :
#     print(k,"=",dic1[k])
#
# print(dic1.keys())
# print(dic1.values())
k = dic1.keys()
print(type(list(k)))
for i in k :
    print(i)
print(list(k)[2:])
#把字典里每一项转成元祖
# for li in dic1.items() :
#     print(li)

'''--------------------------------------------------------------------------------------------------------------------------------'''
#print("创建文件和文件夹")
