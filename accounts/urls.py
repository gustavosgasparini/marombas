from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', views.profile_page, name='profile'),
    path('<int:pk>/about/', views.about_page, name='about'),
    path('<int:pk>/photos/', views.photos_page, name='photos'),
    path('<int:pk>/photos/add-photos/', views.add_photos_page, name='add-photos'),
    path('<int:pk>/my_account/', views.my_account_page, name='my_account'),
    path('<int:pk>/my_account/password/', views.change_password, name='change_password'),
    path('<int:pk>/post/delete/', views.delete_post_prof_page, name='delete_post_prof'),
]