from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#注册
#增加Grade的时候同时增加2个student  (admin.TabularInline与admin.StackedInline只是显示格式不一样)
class StudenInfo(admin.TabularInline):
    model= Students
    extra = 2

#修改界面

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    inlines = [StudenInfo]
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete'] #要显示的属性
    list_filter = ['gname']#过滤器
    search_fields = ['gname']#搜索字段，按照gname搜索
    list_per_page = 5 #分页
    #添加、修改页属性
    #fields = ['ggirlnum','gdate']# 修改属性的顺序
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ]#给属性分组  fields与fieldsets不能同时使用
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender :
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    def name(self):
        return self.sname
    name.short_description = "姓名"
    search_fields = ['gname']
    list_display = ['pk',name,'sgrade','isDelete','sage',gender]
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentsAdmin)
#可以用装饰器来代替以上两句@admin.register(Students)

