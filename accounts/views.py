# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})
