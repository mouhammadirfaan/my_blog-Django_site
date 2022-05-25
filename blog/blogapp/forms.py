from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from blogapp.models import Post, Comments

class Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("author","title","text")

        Widget = {
            "title": forms.TextInput(attrs={'class':'textinputclass'})
            "text": forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentsForm(forms.ModelForm):

    class Mete:
        model = Comments
        field = ("auther","text")

        Widget = {
            "author": forms.TextInput(attrs={'class':'textinputclass'})
            "text": forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }


