from django import forms

class loginForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    # psw = forms.CharField()