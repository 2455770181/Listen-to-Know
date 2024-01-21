"""
URL configuration for Listen_to_Know project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include

"""
    url是Django 1.x中的写法,在Django2.1中，开始舍弃Django1.x中的url写法。在Django2.x中，描写url配置的有两个函数path和re_path，re_path()函数可以看做是django 1.x中的url函数,即可以在路径中使用正则。
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^basic_function/',include('basic_function.urls'))的意思是网址的最终路径由两部分拼接：域名/basic_function/basic_function.urls中的path里的路径
    re_path(r'^basic_function/',include('basic_function.urls'))
]
