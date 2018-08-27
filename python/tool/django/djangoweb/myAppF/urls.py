from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$', views.index),
    url('^(\d+)/(\d+)$',views.detail) , #()是组的概念，传入匹配值
    url('^grades/$',views.grades),
    url('^students/$',views.student),
    url('^grades/(\d+)/$',views.studentgrade),
]
