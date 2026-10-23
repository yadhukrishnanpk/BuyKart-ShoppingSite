from django.urls import path
from . import views

urlpatterns = [
   path('mydashboard/', views.dashboard,name='dashboard'),
   path('contact/', views.contact,name='contact'),
   path('about/', views.about_view,name='about'),
   path('privacy_policy/', views.privacy_policy,name='privacy_policy'),
   path('terms&condition/', views.termsandcondition,name='terms&condition'),

]

