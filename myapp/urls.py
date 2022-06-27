from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.welcome,name="welcome"),
    path('sign-up/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('home/',views.Index_view,name="home"),
    path('^profile/',views.profile,name="profile"),
    path('^myprofile/$',views.user_info,name="user_profile"),
    path('^add-product/$',views.new_product,name="add_product"),
    path('signout/',views.signout,name='signout'),
    path('chat/',views.chat,name='chat'),
    path('send/',views.send,name='send'),
]