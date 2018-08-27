from django.db import models

# Create your models here.
#不需要定义逐渐，自动生成，并自动增加


class Grades(models.Model) :
    gname     = models.CharField(max_length=20)
    gdate     = models.DateField()
    ggirlnum  = models.IntegerField()
    gboynum   = models.IntegerField()
    isDelete  = models.BooleanField(default=False)
    def __str__(self):
        return self.gname

class Students(models.Model) :
    sname    = models.CharField(max_length=20)
    sgender  = models.BooleanField()
    sage     = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade   = models.ForeignKey("Grades",on_delete=models.CASCADE,)
    def __str__(self):
        return self.sname
