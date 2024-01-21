from django.contrib import admin
from django.urls import path
from basic_function import views
"""
    该app原本没有urls.py，需要自行创建
"""
urlpatterns = [
    # 这里不要用re_path
    path('login/', views.LoginView.as_view())
]
