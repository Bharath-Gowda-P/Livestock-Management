from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_view, name="logout"),   
    path('add/', views.add, name="add"),  
    path('delete/<int:id>', views.delete_view, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
]
