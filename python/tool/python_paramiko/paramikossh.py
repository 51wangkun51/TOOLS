import os,paramiko,stat
#private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname","22","wangkun","Changeme_123")
#ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', key=private_key)
cmd = ". /opt/PRS/server/sv;displayVersion -a"
stdin ,stdout ,stderr = ssh.exec_command(cmd)
result = stdout.read()
if not result :
    result = stderr()
ssh.close()

import paramiko
#private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
#创建SSH对象
ssh = paramiko.SSHClient()
#把要连接的机器添加到known_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='192.168.1.96', port=22, username='morra', password='123456')
#ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', key=private_key)
cmd = 'ps'
#cmd = 'ls -l;ifconfig'       #多个命令用;隔开
stdin, stdout, stderr = ssh.exec_command(cmd)
result = stdout.read()
if not result:
    result = stderr.read()
ssh.close()
print(result.decode())

