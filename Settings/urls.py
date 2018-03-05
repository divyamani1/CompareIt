"""Compareit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from Compareit.views import Home_view, post_original, post_user, report_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_view, name='Home'),
    path('save-text-1/', post_original, name='post_original_url'),
    path('save-text-2/', post_user, name='post_user_url'),
    path('report/', report_view, name='report_view_url'),
]
