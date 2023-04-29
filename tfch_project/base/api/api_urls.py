from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('concerts/', views.getConcerts),
    path('concerts/<str:primary_key>', views.getConcert),
]