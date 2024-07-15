# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Correct import
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use CustomUserCreationForm
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()  # Use CustomUserCreationForm
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def main(request):
    return render(request, 'main.html')