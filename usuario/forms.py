from django import forms

class CreateUserForm(forms.Form):
    Username = forms.CharField(max_length=20, label='Nombre de Usuario:')
    Password = forms.CharField(max_length=10, label='Password: ', widget=forms.PasswordInput)
    Check_Password = forms.CharField(max_length=10, label='Confirmar password: ', widget=forms.PasswordInput)
    Email = forms.EmailField(label='E-mail: ')
    First_name = forms.CharField(max_length=60, label='Nombre: ')
    Last_name = forms.CharField(max_length=80, label='Apellido: ')

class LoginUserForm(forms.Form):
    Username = forms.CharField(max_length=20, label='Nombre de Usuario: ')
    Password = forms.CharField(max_length=10, label='Password: ', widget=forms.PasswordInput)
