from django import forms

class loginForm(forms.Form):
    Email = forms.EmailField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email',
                'type':'email'
            }
        )
    )
    Password = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Enter Your Password',
                'type':'password'
            }
        )
    )