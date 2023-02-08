from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class noviKorisnikForm(ModelForm):
    name = forms.TextInput()
    user_name = forms.TextInput()
    email = forms.EmailField()
    password = forms.TextInput()
    class Meta:
        model = Korisnik
        fields = ['name','user_name','email','password']

class novaReputacijaForm(ModelForm):
    points = forms.IntegerField()
    user_name = forms.Select()
    class Meta:
        model = Reputacija
        fields = ['points','user_name']	

class noviKomentarForm(ModelForm):
    comment = forms.TextInput()
    user_name = forms.SelectMultiple()
    class Meta:
        model = Komentar
        fields = ['comment','user_name']

class noviBlogForm(ModelForm):
    theme = forms.TextInput()
    date = forms.DateField()
    time = forms.TimeField()
    comment = forms.SelectMultiple()
    class Meta:
        model = Blog
        fields = ['theme','date','time','comment']	