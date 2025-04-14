from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_plan, name='create_plan'),
    path('solution/<int:pk>/', views.view_solution, name='view_solution'),
    path('plans/', views.plan_list, name='plan_list'),
    path('delete/<int:pk>/', views.delete_plan, name='delete_plan'),
    path('steps/', views.view_steps, name='view_steps'),
    path('applications/', views.view_applications, name='view_applications'),
] 