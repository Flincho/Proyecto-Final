from django.urls import path
from accounts import views


app_name = 'accounts'
urlpatterns = [
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
    path('user/update', views.user_update, name='user-update'),
    path('biography/update', views.bio_update, name='bio-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path('profile', views.profile, name='profile'),
]
