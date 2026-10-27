from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from item.models import Category, Item
from conversation.models import ConversationMessage,Conversation
from .serializers import ItemSerializer,CategorySerializer,ConversationMessageSerializer,ConversationSerializer,UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(members__in=[user.id])

class ConversationmessageViewset(viewsets.ModelViewSet):
    queryset = ConversationMessage.objects.all()
    serializer_class= ConversationMessageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
            user = self.request.user
            return ConversationMessage.objects.filter(conversation__members__in=[user.id])
    


