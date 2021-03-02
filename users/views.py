from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Profile
# Create your views here.

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form':form
    }
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile': profile,
    }
    return render(request, "users/profile.html", context)

@login_required
def profile_update(request):
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {
        'form':form
    }
    return render(request, "users/profile_update.html", context)