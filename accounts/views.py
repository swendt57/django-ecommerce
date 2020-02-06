from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import UserLoginForm, UserRegistrationForm, ChangePasswordForm


# Create your views here.


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))


def login(request):
    """Return the login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is invalid')

    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, 'Unable to register your account')
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {"registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


def change_password(request):
    """Change user password page"""
    if not request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'change_password_form': form
    })

# def change_password(request):
#     """Change user password page"""
#     change_password_form = ChangePasswordForm(request.POST)
#     print('in change password')
#     # if request.user.is_authenticated:
#     #     return render(request, 'change_password.html', {'change_password_form': change_password_form})
#
#     if request.method == "POST":
#
#         # if login_form.is_valid():
#         #     user = auth.authenticate(username=request.POST['username'],
#         #                              password=request.POST['password'])
#         #
#         print('in the submit: ' + request.POST['new_password'])
#         for item in request.POST:
#             print(str(item)+'\n')
#
#         print(str(request.POST))
#
#         if change_password_form.is_valid():
#             user = User.objects.get(email=request.user.email)
#             print(user)
#             user.set_password(request.POST['confirm_password'])
#             user.save()
#
#     return render(request, 'change_password.html', {'change_password_form': change_password_form})
