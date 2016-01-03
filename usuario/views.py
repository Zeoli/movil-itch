from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin, logout as authlogout, authenticate
from django.http import HttpResponseRedirect
from usuario.forms import CreateUserForm, LoginUserForm
# Create your views here.

def Main(request):
    return HttpResponse("Hola Mundo")

def Create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            msg = {}
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['Username']
            psw = form.cleaned_data['Password']
            psw2 = form.cleaned_data['Check_Password']
            email = form.cleaned_data['Email']
            first_name = form.cleaned_data['First_name']
            last_name = form.cleaned_data['Last_name']
            if psw != psw2:
                msg['error'] = 'No coinciden'
                return render_to_response('register_form.html', msg)
            new_user = User.objects.create_user(username, email, psw)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            # redirect to a new URL:
            return redirect('/login')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateUserForm()
    return render(request, 'register_form.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            msg = {}
            username = form.cleaned_data['Username']
            psw = form.cleaned_data['Password']
            user = authenticate(username=username, password=psw)
            if user is not None:
                if user.is_active:
                    authlogin(request, user)
                    return redirect('/')
                else:
                    msg['error'] = 'Cuenta inhabilitada'
                    return render_to_response('login.html', msg)
            else:
                msg['error'] = 'Datos incorrectos'
                return render_to_response('login.html', msg)
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})
