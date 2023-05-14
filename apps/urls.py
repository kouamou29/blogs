from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index' ),
    path('singup/', views.singup, name='singup'),
    path('login/', views.login_user, name='login'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
