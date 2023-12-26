from django import forms

from .models import *


class AddMembersForm(forms.ModelForm):
    class Meta:
        model=AddMembers
        fields="__all__"