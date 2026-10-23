
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/',views.Signup, name='signup'),
    path('login/',views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
