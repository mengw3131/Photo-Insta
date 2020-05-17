from django.contrib import admin
from django.urls import include, path

from Insta.views import (HelloWorld, PostsView, PostDetailView, UserDetailView, PostCreateView, 
                         PostUpdateView, PostDeleteView, addLike)

urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name = 'helloworld'),
    path('', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name = 'user_detail'),
]