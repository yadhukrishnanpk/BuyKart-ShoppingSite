from django import forms
from .models import Item

class NewitemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields =('category', 'name','description','price','image',)
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full p-3 border border-gray-300 rounded-xl'}),
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-xl', 'placeholder': 'Item name'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-5 border border-gray-300 rounded-xl', 'rows': 2,'placeholder': 'Item Description'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-xl', 'placeholder': '0.00'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-xl'}),
        }
        
        
class EdititemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields =('category', 'name','description','price','image','is_sold')
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item name'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-5 border border-gray-300 rounded-xl', 'rows': 2,'placeholder': 'Item Description'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': '0.00'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
            'is_sold': forms.CheckboxInput(attrs={'class': 'w-5 h-5 text-green-600 bg-gray-100 border-gray-300 rounded focus:ring-green-500 focus:ring-2 cursor-pointer'})
        }