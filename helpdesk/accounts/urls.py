from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('dashboard/', views.dashboard),
    path('role/', views.role),
    path('user/', views.user),
    path('project/', views.project),
    path('ticket/', views.ticket),
    path('profile/', views.profile),
]