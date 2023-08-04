from django.urls import path
from water import views

urlpatterns =[
    path("new/", views.top_new, name="top_new")
]