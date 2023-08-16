from django.urls import path
from water import views

urlpatterns =[
    path('dashboard/', views.dashboard, name='dashboard'),
]