from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects_page,name='projects')
]
