from django.urls import path
from blogs.views import add_permission, change_password, register, profile


app_name = "blogs"

urlpatterns = [
    path('profile/<str:username>/', profile, name='profile'),
    path('change-password/<str:username>/', change_password, name='change-password'),
    path('register/', register, name='register'),   
    path('add-permissions/<str:username>/', add_permission, name='add-permissions'),
]