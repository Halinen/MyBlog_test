# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:urls.py
@time:2018/9/14 19:07
"""
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index,name='index'),
    re_path(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    re_path(r'^edit/action$', views.edit_action, name='edit_action'),
]
