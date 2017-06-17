# -*- coding: utf-8 -*-
from django.conf.urls import url
from chat import views
urlpatterns = [
	url(r'^api/chat/$', views.chat, name='chat'), # api that returns PTT articles.
]
