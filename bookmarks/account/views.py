from django.contrib import messages
# from django.http import HttpResponse
# from django.contrib.auth import login, authenticate
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import CustomRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def edit(request):
    # retrieving forms previously assigned to a user
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == "POST":
        # adding additional info to pre-generated forms
        user_form = UserEditForm(data=request.POST)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Udało się')
        messages.error(request, 'Błąd')
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def dashboard(request):
    return render(request, 'base.html', {'section': 'dashboard'})


def register(request):
    registration_form = CustomRegistrationForm()
    if request.method == "POST":
        registration_form=CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data['password_2'])

            # new_user.is_active = False
            # add emial confirmation
            new_user.save()

            Profile.objects.create(user=new_user)

            return render(request, 'account/registration_done.html', {'new_user':new_user})
    return render(request,'account/register.html', {'form': registration_form})





# standard user login view, no fireworks here

# def user_login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse('gotowe')
#                 return HttpResponse('konto nieaktywne')
#         return HttpResponse('błędny login lub hasło')
#     return render(request, 'account/login.html', {'form':for
