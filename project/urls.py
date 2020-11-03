from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.latern, name = "start"),
    path('project/',views.article1, name = "article1"),
    path('project/article2',views.article2, name = "article2"),
    path('project/article3',views.article3, name = "article3"),
    path('project/article4',views.article4, name = "article4"),
]
