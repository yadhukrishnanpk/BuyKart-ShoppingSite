
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:item_pk>/', views.NewChat,name='chat'),
    path('chatbox/', views.chatBox,name='chatbox'),
    path('<int:pk>/', views.DetailedChat,name='detailchat'),
    path('conversations/<int:pk>/delete/', views.delete_conversation, name='delete_conversation'),
]
