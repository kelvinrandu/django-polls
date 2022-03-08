from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.get_name, name='add'),
     path("create/", views.CreatePersona.as_view(), name="create"),
]
