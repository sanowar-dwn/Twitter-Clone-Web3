from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Company
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            comapny = Company.objects.create(name=user.username, created_by=user)

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})