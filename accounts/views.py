from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password1'] and request.POST['password2'] != '':
        #user wants an account
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username = request.POST['username'])
                    return render(request, 'signup.html', {'error':'Username "{}" already exists!'.format(request.POST['username'])})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                    auth.login(request, user)
                    return redirect('home')
            else:
                #passwords do not match
                return render(request, 'signup.html', {'error':'Passwords do not match!'})
        else:
            #fields empty
            return render(request, 'signup.html', {'error':'Fields must not be empty!'})

    else:
        #user wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password'] != '':
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error':'Username or password is incorrect'})
        else:
            #fields empty
            return render(request, 'login.html', {'error':'Fields must not be empty!'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
