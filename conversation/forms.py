from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):  
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 text-xs sm:text-sm border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500 resize-none min-h-[42px] max-h-32',
                'rows': 1,
                'placeholder': 'Type a message...'
            }),
        }



    
