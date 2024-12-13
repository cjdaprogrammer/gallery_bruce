from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_meme, name='add_meme'),
    path('delete/<int:meme_id>/', views.delete_meme, name='delete_meme'),
]
