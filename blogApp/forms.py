from django import forms
from .models import Article,Author,Comment,Category
from .models import User
from django.contrib.auth.forms import UserCreationForm


class createForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'category',
            'title',
            'image',
            'body'
        ]


class registration(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class creteAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'author_image',
            'details'
        ]


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'post_comment'
        ]

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]