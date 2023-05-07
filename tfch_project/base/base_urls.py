from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register_user, name="register"),
    path("", views.home_page, name="home page"),
    path("profile/<str:primary_key>/", views.user_profile, name="user profile"),
    path("update-user/", views.update_user, name="update-user"),
    path("program/<str:primary_key>/", views.program, name="program"),
    path("program/", views.create_a_program, name="create program"),
    path(
        "modification/<str:primary_key>/", views.modify_program, name="modify program"
    ),
    path("concert/<str:primary_key>/", views.concert, name="concert"),
    path("new_concert/", views.create_a_concert, name="create concert"),
    path(
        "concert_modification/<str:primary_key>/",
        views.modify_concert,
        name="modify concert",
    ),
    path("error/", views.error, name="error"),
]
