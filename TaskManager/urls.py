from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]