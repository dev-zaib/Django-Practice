from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_home, name='create_home'),
    path('<int:create_id>/', views.create_detail, name='create_detail'),
]