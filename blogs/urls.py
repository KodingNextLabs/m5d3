from django.urls import path
from blogs.views import JARoom, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, SubscribeFormView, TestPost, add_permission, add_post, change_password, ja_room, register, profile, test_post, thanks


app_name = "blogs"

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/<str:username>/', profile, name='profile'),
    path('change-password/<str:username>/', change_password, name='change-password'),
    path('accounts/login/', register, name='register'),   
    path('add-permissions/<str:username>/', add_permission, name='add-permissions'),
    path('add-post/', PostCreateView.as_view(), name='add-post'),
    path('test-post/', TestPost.as_view(), name='test-post'),
    path('ja-room/', JARoom.as_view(), name='ja-room'),
    path('thanks/', thanks, name='thanks'),
    path('subscribe/', SubscribeFormView.as_view(), name='subscribe'),
]