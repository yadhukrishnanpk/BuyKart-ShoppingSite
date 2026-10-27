from rest_framework import serializers
from item.models import Item,Category
from conversation.models import Conversation,ConversationMessage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username']
        
class ItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Item
        fields =['id', 'name', 'description', 'price', 'image', 'is_sold', 'created_by', 'created_at']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['name']
        
class ConversationMessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ['id', 'conversation', 'content', 'created_at', 'created_by']
        
class ConversationSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    message = ConversationMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'item', 'members', 'message', 'created_at', 'modified_at']       

