from typing import Any
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Posts, Category , Comment, ProfileUser
from django.core.exceptions import ValidationError

class Userform(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class":"py-3 px-4 rounded-xl w-80 border-teal-700 border-solid",
            'placeholder':"Username"
        })
        self.fields["email"].widget.attrs.update({
            "class":"py-3 px-4 rounded-xl w-80 border-teal-700 border-solid",
            'placeholder':"Email"
        })
        self.fields["password1"].widget.attrs.update({
            "class":"py-3 px-4 rounded-xl w-80 border-teal-700 border-solid",
            'placeholder':"Password"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"py-3 px-4 rounded-xl w-80 border-teal-700 border-solid",
            'placeholder':"Confirm password"
        })
    
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
    
    

class PostForm(forms.ModelForm):
    

    class Meta:
        model = Posts
        
        fields = ('title', 'description', 'user', ) 
        error_messages = ''   
    
    def clean_title(self):
        
        title =  self.cleaned_data.get('title')
        if len(title) <  7:
            raise forms.ValidationError('vous entez au moins 10 caratère')
        return title
    
    def clean_description(self):
        
        description =  self.cleaned_data.get('description')
        if len(description)  < 10:
            raise forms.ValidationError('votre post doit avoir moins 100 de caratere"')
        return description
    

class FormProfileUser(forms.ModelForm):
    class Meta:
        model = ProfileUser
        
        fields = ('image', 'bio')       
      
      