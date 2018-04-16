from django.urls import path
from . import views

urlpatterns = [
    #path('profile/<str:username>/', views.profile),
    #path('profile/<slug:username>/', views.profile),
    #El orden es importante se debe acomodar segun especifidad del parametro
    path('profile/28/', views.profile),
    path('profile/<int:username>/', views.profile),
    path('profile/<slug:article>', views.article),
    path('profile/', views.profile),
]