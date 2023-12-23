"""
URL configuration for core project.
#!/usr/bin/env python
# -*- coding: utf8 -*-
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.docgurnal.views import *
app_name = 'docgurnal'
urlpatterns = [
    #path('admin/', admin.site.urls),

    path('gurnal/', gurnalView.as_view(), name='gurnal'),

    path('gurnal/update/<int:pk>/', gurnalUpdate.as_view(), name='gurnalUpdate'),
    path('gurnal/detail/<int:pk>/', gurnalDetail.as_view(), name='gurnalDetail'),
    path('gurnal/create/', gurnalCreate.as_view(), name='gurnalCreate'),
    path('gurnal/delete/<int:pk>/', gurnalDelete.as_view(), name='gurnalDelete'),

    path('gurnal/download/', downloadDoc, name='gurnalDownload'),
]