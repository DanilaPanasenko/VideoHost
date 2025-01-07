from django.urls import path
from . import views
from django.contrib.auth import views as auth
from django.contrib.auth.views import LogoutView
from .views import Login, register
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', Login, name='login'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
