from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('captcha',views.send_email_captcha,name='captcha'),
    path('logout',views.logout,name='logout'),
    path('pub_blog',views.pub_blog,name='pub_blog'),
]
