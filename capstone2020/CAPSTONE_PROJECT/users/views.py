from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #flash message - one-time alerts.
            messages.success(request, f'Account created for {username}!')
            return redirect('app-home')
        else: 
            messages.warning(request, f'Failed. Please see below and try again.')
            return render(request, 'users/register.html', {'form': form})
    else:        
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

#TODO add login view + template + route