from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("create/", views.CreatePersona.as_view(),name="create"),
  
]
