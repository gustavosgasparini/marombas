from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', views.PostPage, name='post_page'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('<int:pk>/comment/delete', views.delete_commment, name='delete_comment'),
    path('like/', views.like_post, name='like_post'),
]