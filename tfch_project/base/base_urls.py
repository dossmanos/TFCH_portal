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

    path('program/<str:primary_key>/', views.program, name='program'),
    path('program/', views.create_a_program, name='create program'),
    path('modification/<str:primary_key>/', views.modify_program, name='modify program'),

    path('concert/<str:primary_key>/', views.concert, name='concert'),
    path('concert/', views.create_a_concert, name='create concert'),
    path('concert_modification/<str:primary_key>/', views.modify_concert, name='modify concert'),

    path('error/',views.error,name='error'),
]