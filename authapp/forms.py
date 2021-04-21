import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from icecream import ic

from authapp.models import ValAuth, ClientProfile
from django.forms import forms, ModelForm, HiddenInput

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = ValAuth
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = ValAuth
        # fields = ('username','first_name','last_name','companyName', 'email', 'activation_key_expires','activation_key')
        # fields = '__all__'
        fields = ('username','first_name','last_name','companyName', 'email')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


    def save(self, commit=True):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UserProfileForm(ModelForm):
    class Meta:
        model = ValAuth
        fields = ('username','password', 'companyName')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # ic(field_name)
            # ic(field.widget.__dict__)
            if field_name == 'password':
                field.widget = HiddenInput()
            else:
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''