from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name="index"),
    path('blog/',views.detail,name="detial")
]