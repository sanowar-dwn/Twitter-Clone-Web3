from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company
from ..device.models import Device
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


@login_required
def company_dashboard(request):
    company = request.user.company
    devices = Device.objects.filter(company=company)
    context = {'company':company, 'devices':devices}
    return render(request, 'dashboard.html', context)