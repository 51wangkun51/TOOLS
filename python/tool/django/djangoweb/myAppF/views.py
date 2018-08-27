from django.shortcuts import render
from .models import Grades,Students

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("fist page,sumdb is a database")
def detail(request,num,num2):
    print("num1 = %s ,num2 = %s"%(num,num2))
    return HttpResponse('detail message %s -- %s' % (num,num2))

def grades(request):
    #去模板里取数据
    gradelist = Grades.objects.all();
    #将数据传递给模板，模板再渲染页面，最终返给浏览器
    return render(request,'myAppF/grades.html',{"grades" : gradelist})

def student(request):
    studentlist = Students.objects.all()
    return render(request,'myAppF/students.html',{"students":studentlist})
def studentgrade(request,num):
    print("num = %s" % num)
    grade = Grades.objects.get(pk = int(num) )
    studentlist = grade.students_set.all()
    return  render(request,'myAppF/students.html',{"students":studentlist})








