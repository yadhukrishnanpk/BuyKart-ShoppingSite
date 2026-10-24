
from django.urls import path
from . import views

urlpatterns = [
   path('browse/', views.items,name='items'),
   path('new/', views.newItem,name='new'),
   path('<int:pk>/', views.detail,name='detail'),
   path('<int:pk>/delete/', views.delete,name='delete'),
   path('<int:pk>/edit/', views.editItem,name='edit'),
   
   path('categories/', views.manage_categories, name='manage_categories'),
   path('category/new/', views.add_category, name='add_category'),
   path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
   path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
   ]
