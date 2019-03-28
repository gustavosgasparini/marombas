from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', views.PostPage, name='post_page'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
]