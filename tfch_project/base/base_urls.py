from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register_user,name='register'),

    path('', views.home_page, name='home page'),
    path('room/<str:primary_key>/', views.room, name='chat room'),
    path('profile/<str:primary_key>/', views.user_profile, name='user profile'),

    path('create-room/', views.create_a_chat_room, name='create-room'),
    path('update-room/<str:primary_key>/', views.update_room, name='update-room'),
    path('delete-room/<str:primary_key>/', views.delete_a_chat_room, name='delete-room'),

    path('update-user/', views.update_user, name='update-user'),

    path('delete-post/<str:primary_key>/', views.delete_a_post, name='delete-post'),
    
    path('topics/', views.topics_page, name='topics'),
    path('activities/', views.activities_page, name='activities'),
]