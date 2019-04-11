"""Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
import page.views


urlpatterns = [
    url(r'^page/', include('page.urls')),
    url(r'admin/', admin.site.urls),
    url(r'login/', page.views.user_login, name='user_login1'),
    url(r'^$', page.views.user_login, name='user_login'),
    url(r'^logout$', page.views.user_logout, name='user_logout'),
    url(r'^register$', page.views.user_register, name='register'),

]