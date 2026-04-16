from django import forms

from .models import Comment

class CommentForm(forms.form.ModelForm):
    class Meta:
        model = Comment
        fields =['name', 'email', 'body']