import paramiko
import paramiko
#private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
transport = paramiko.Transport(('192.168.1.96', 22))
transport.connect(username='morra', password='357447218')
#transport.connect(username='wupeiqi', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('123.py', '/tmp/test.py')  # 将123.py 上传至服务器 /tmp下并改名为test.py
sftp.get('remove_path', 'local_path')  # 将remove_path 下载到本地 local_path
transport.close()


'''merge ssh and sftp'''
import paramiko

class SSHConnection(object):

    def __init__(self, host='192.168.11.61', port=22, username='alex',pwd='alex3714'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self,local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

ssh = SSHConnection()
ssh.connect()
r1 = ssh.cmd('df')
ssh.upload('s2.py', "/home/alex/s7.py")
ssh.close()