from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # :8080/boards/
    path('new/', views.new), # :8080/boards/new
    path('create/', views.create), # :8080/boards/create
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]