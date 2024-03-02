from django import forms
from .models import Comment

# class CarForm(forms.ModelForm):
#     class Meta: 
#         model = car
#         fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']
