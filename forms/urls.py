from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create, name='add'),
    path('update/<str:pk>', views.update, name='update'),
    path("create/", views.CreatePersona.as_view(),name="create"),
  
]
