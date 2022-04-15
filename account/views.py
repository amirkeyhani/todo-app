from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UpdateForm, UserRegistrationForm, userform, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'registration created successfully')
            return redirect('/')
    else:
        fm = RegistrationForm()

    return render(request, 'account_files/signup.html', context={'fm': fm})

def home(request):
    form = userform()
    
    return render(request, 'home.html', context={'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfully for {username}! \t')
            return redirect('/')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', context={'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user)
        u.delete()
        return HttpResponse('Your account deleted successfully')
    return render(request, 'delete-account.html')

def update_profile(request):
    if request.method == 'POST':
        u_fm = UpdateForm(data=request.POST, instance=request.user)
        if u_fm.is_valid():
            u_fm.save()
            messages.success(request, 'Profile updated')
    else:
        u_fm = UpdateForm(instance=request.user)
        
    return render(request, 'update-profile.html', context={'u_fm': u_fm})