from django import forms

class CreateUserForm(forms.Form):
    Username = forms.CharField(max_length=20)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    Check_Password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    First_name = forms.CharField(max_length=60)
    Last_name = forms.CharField(max_length=80)
    #your_name = forms.CharField(label='Your name', max_length=100)
