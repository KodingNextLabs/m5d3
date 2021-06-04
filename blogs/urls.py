from django.urls import path
from blogs.views import register, profile


app_name = "blogs"

urlpatterns = [
    path('profile/<str:username>/', profile, name='profile'),
    path('register/', register, name='register'),
    
]