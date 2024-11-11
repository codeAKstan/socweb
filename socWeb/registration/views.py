from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})


    else:
        form = UserRegisterForm()
    return render(request, 
                  'registration/register.html',
                  {'form': form})

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html',
                  {'section': 'dashboard'})