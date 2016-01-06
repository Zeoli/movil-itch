from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

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

class PerfilForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super (PerfilForm, self).__init__(*args, **kwargs)
        #self.fields['user'].queryset = User.objects.filter(username=user)
        self.fields['user'].widget.attrs['value'] = User.objects.filter(username=user)[0].pk
        self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['imagen']
        widgets = {
            'user': forms.HiddenInput(),
            'imagen': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'camera'}),
        }
        labels = {
            'numero': 'Numero interior: ',
            'calle': 'Calle: ',
            'colonia': 'Colonia: ',
            'municipio': 'Municipio: ',
            'estado': 'Estado :',
            'ciudad': 'Ciudad: ',
            'pais': 'Pais: ',
        }
