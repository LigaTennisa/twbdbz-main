from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('about/', views.about, name='about'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('courts/', views.courts, name='courts'),
    path('training/', views.training, name='training'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('myprofile/', views.myprofile, name='myprofile'),
]
