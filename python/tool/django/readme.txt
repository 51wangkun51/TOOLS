1、http://edu.51cto.com//center/course/lesson/index?id=228446
2、
3、
4、在需要创建工程的目录 django-admin startproject projectname
5、conda install pymysql
6、z在__init__.py文件中加入如下两句
    import pymysql
    pymysql.install_as_MySQLdb()

7、在setting中配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.数据库类型',
        'NAME': 数据库名
        'USER':''
        'PASSWORD':''
        'HOST':'localhost/IP'
        'PORT':'3306'),
    }
}
8、安装数据库
    解压安装包，手动创建my.ini文件和data文件夹
    C:Windows\system32>mysqld --romve  //删除mysql服务
    C:Windows\system32>mysqld --install //安装mysql服务
    C:Windows\system32>mysqld --initialize //一定要初始化
    C:Windows\system32>net start mysql
    data/wangkun-PC.err文件中会生成一个临时密码

9、新建数据库，打开cmd，mysql -u root -p
    修改root密码set password for root@localhost = passwore('Changeme_123')
9、查看数据库show databases;
 创建数据库create database sumdb;
10、创建我的应用
    进入manage.py级目录，输入python manage.py startapp myAppF 创建名为myAppF的应用
