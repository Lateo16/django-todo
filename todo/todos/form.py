from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Todo


class TodoForm(ModelForm):
    todo = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'todo-item',
            'max_length': 40,
            'size': 40
            }
    ))

    # done = forms.BooleanField(widget=forms.CheckboxInput(
    #     attrs={'class': 'completed'}
    # ))

    class Meta:
        model = Todo
        fields = ['todo',]