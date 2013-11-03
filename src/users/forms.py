from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
    AdminPasswordChangeForm as BaseAdminPasswordChangeForm
    )
from .models import User

class UserCreationForm(BaseUserCreationForm):
    
    class Meta:
        model = User
        
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
        
class UserChangeForm(BaseUserChangeForm):
    def __init__(self, *args, **kwargs):
        super(BaseUserChangeForm, self).__init__(*args, **kwargs)
    class Meta:
        model = User

class AdminPasswordChangeForm(BaseAdminPasswordChangeForm):
    class Meta:
        model = User
