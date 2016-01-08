from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin, logout as authlogout, authenticate
from usuario.forms import CreateUserForm, LoginUserForm, PerfilForm
from .models import Profile
# Create your views here.

def Create(request):
    # if this is a POST request we need to process the form data
    if not request.user.is_authenticated():
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
                #return redirect('/login')
                return HttpResponseRedirect('/')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = CreateUserForm()
        return render(request, 'register_form.html', {'form': form})
    else:
        return redirect('/')

def Login(request):
    if request.method == 'POST':
        msg = {}
        username = request.POST['username']
        psw = request.POST['password']
        if username and psw:
            user = authenticate(username=username, password=psw)
            if user is not None:
                if user.is_active:
                    authlogin(request, user)
                    return HttpResponseRedirect('/')
                else:
                    msg['error'] = 'Cuenta inhabilitada'
                    return  HttpResponseRedirect('/')
            else:
                msg['error'] = 'Datos incorrectos'
                return HttpResponseRedirect('/')
        else:
            HttpResponseRedirect('/')
    return render(request, 'index.html')

def Logout(request):
    authlogout(request)
    return redirect('/')

@login_required(login_url='/login', redirect_field_name='')
def ProfileView(request):
    usuario = User.objects.get(username=request.user.username)
    try:
        perfil = Profile.objects.get(user=usuario)
    except Profile.DoesNotExist:
        return redirect('/edit/perfil/')
    return render(request, 'perfil_view.html', {'perfil': perfil})


@login_required(login_url='/login', redirect_field_name='')
def ProfileEdit(request):
    if request.method == 'POST':
        form = PerfilForm(request.user.username, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        try:
            user = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            form = PerfilForm(request.user.username)
            return render(request, 'perfil.html', {'form': form})
        form = PerfilForm(request.user.username, instance=user)
    return render(request, 'perfil.html', {'form': form})
