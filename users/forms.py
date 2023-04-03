from django import forms
from allauth.account.forms import LoginForm,SignupForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

  
  
class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False



class Register(SignupForm):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class':'input-group',
        'name':'firstname',
        'id':'firstname',
        'type':'text',
        'placeholder':'firstname'
        })
        self.fields['lastname'].widget.attrs.update({'class':'input-group',
        'name':'lastname',
        'id':'lastname',
        'type':'text',
        'placeholder':'lastname'
        })
        self.fields['username'].widget.attrs.update({'class':'input-group',
        'name':'username',
        'id':'username',
        'type':'text',
        'placeholder':'username'
        })
        self.fields['email'].widget.attrs.update({'class':'input-group',
        'name':'email',
        'id':'email',
        'type':'email',
        'placeholder':'email'
        })
        self.fields['password1'].widget.attrs.update({'class':'input-group',
        'name':'password1',
        'id':'password1',
        'type':'password',
        'placeholder':'password1',
        'minlength':'8'
        })
        self.fields['password2'].widget.attrs.update({'class':'input-group',
        'required':'', 
        'name':'password2',
        'id':'password2',
        'type':'password',
        'placeholder':'password2',
        'minlength':'8'
        })
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username','email','password1', 'password2']

    def clean_password(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if  password1 != password2:
            raise ValidationError({'password2':'password mismatch'})

        return password2

 
class CustomLoginForm(LoginForm):
     def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({'class':'input-group',
        'name':'username',
        'id':'username',
        'type':'text',
        'placeholder':'username or email'
        })
        self.fields['password'].widget.attrs.update({'class':'input-group',
        'name':'password',
        'id':'password',
        'type':'text',
        'placeholder':'password'})

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required=False
        self.fields['username'].widget.attrs.update({'class':'input-group',
        'name':'username',
        'id':'username',
        'type':'text',
        'placeholder':'username'
        })
        self.fields['email'].required=False
        self.fields['email'].widget.attrs.update({'class':'input-group',
        'name':'email',
        'id':'email',
        'type':'email',
        'placeholder':'email'
        })
    class Meta :
        model = User
        fields =  ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=TinyMCE(attrs={'class':'input-group',
        'name':'bio',
        'id':'bio',
        'type':'text',
        'placeholder':'bio',
        'cols': 50, 'rows': 30}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required=False
        self.fields['image'].widget.attrs.update({'class':'input-group',
        'name':'image',
        'id':'image',
        'type':'image',
        'placeholder':'',
        })
        self.fields['bio'].required=False


    class Meta:
        model = Profile
        fields = ['bio','image']

