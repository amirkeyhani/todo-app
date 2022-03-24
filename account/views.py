from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegistrationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! \t')
            return redirect('/')
    else:
        form = UserRegistrationForm()
            
    return render(request, 'account_files/signup.html', context={'form': form})