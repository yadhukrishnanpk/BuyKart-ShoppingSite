from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =('-modified_at',)
    def __str__(self):
        member_names = ", ".join([user.username for user in self.members.all()])
        return f"Chat for '{self.item.name}' ({member_names if member_names else 'No members'})"
         
class ConversationMessage(models.Model):
    conversation =models.ForeignKey(Conversation,related_name='message',on_delete=models.CASCADE)
    content =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    created_by =models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f" Chat Initiated By {self.created_by}"
