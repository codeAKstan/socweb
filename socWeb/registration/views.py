from django.shortcuts import render
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
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

def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 
                  'registration/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})