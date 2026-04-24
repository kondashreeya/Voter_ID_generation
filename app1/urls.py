from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('view/<int:id>/', views.view),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]