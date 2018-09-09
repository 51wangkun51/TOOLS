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
    进入manage.py级目录，输入python manage.py startapp myAppF 创建名为myAppF的应用将其加入到主应用的setting文件中
11、进入子应用设置models，与数据库中的表一一对应，class
12、生成数据库表，
    生成迁移文件，python manage.py makemigrations
    执行迁移，python manage.py migrate
13、测试操作数据进入shell,
    python manage.py shell
    引入响应的包
    from myAppF.models improt Grades,Students
    from django.utils import timezone
    fome datetime import *
    Grades.objects.all()查看所有数据
    grade1 = Grades()添加数据，常见类型对象的实例
    grade1.gname="music"
    grade1.gdate=datetime(year=2017,month=4,day=17)
    grade1.ggirlnum=3
    grade1.gboynum=8
    grade1.save()
    g = Grades.object.get(pk =1)查询数据pk=1相当于id=1
    grade1.gboynum = 9修改
    grade1.save()
    grade1.delete()删除
    对象名.关联的类名小写_set_all()查询关联数据
14、启动服务器 python manage.py sunserver ip:port
    ip不谢表示本机
    端口号默认是8000
    所以本机测试可直接写成python manage.py sunserver
15、配置Admin应用，在setting中的INSTALLED_APPS中添加
    'django.contrib.admin'
16、创建管理员用户
    在cmd中执行python manage.py createsuperuser
    按照提示输入用户名密码等信息,重启数据库net stop mysql/net start mysql
    登录http://127.0.0.1:8000/admin/
17、汉化
    修改setting中
    LANGUAGE_CODE = 'zh-Hans'
    TIME_ZONE = 'Asia/Shanghai'
18、管理数据表
    修改\myAppF\admin.py这个文件，把表信息注册到这里
    from .models import Grades,Students
    #注册
    admin.site.register(Grades)
    admin.site.register(Students)
19、html页面中显示值
    {{输出值，可以是变量，也可以是对象.属性}}
    {%执行代码段%}
20、开发页面流程
    写模板--html
    写视图---写响应的函数
    配置url---写、url的筛选和视图的对应关系
21、如果增加表，则重新生成迁移文件，再执行迁移文件
    如果修改字段，则删除数据库后再征程迁移文件，执行迁移文件
22、
23、
24、
25、
26、
27、
28、启动应用
    启数据库net start mysql  （以管理员权限运行cmd）
    启服务python manage.py sunserver
    登录http://127.0.0.1:8000/
29、
