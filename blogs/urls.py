from django.urls import path
from blogs.views import JARoom, TestPost, add_permission, add_post, change_password, ja_room, register, profile, test_post


app_name = "blogs"

urlpatterns = [
    path('profile/<str:username>/', profile, name='profile'),
    path('change-password/<str:username>/', change_password, name='change-password'),
    path('accounts/login/', register, name='register'),   
    path('add-permissions/<str:username>/', add_permission, name='add-permissions'),
    path('add-post/', add_post, name='add-post'),
    path('test-post/', TestPost.as_view(), name='test-post'),
    path('ja-room/', JARoom.as_view(), name='ja-room'),
]