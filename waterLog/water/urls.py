from django.urls import path
from water import views

urlpatterns =[
    path("new/", views.top_new, name="top_new"),
    path("edit/<int:water_id>/",views.edit_water_consumption, name="edit_water_consumption")
]