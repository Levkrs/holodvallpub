from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from icecream import ic

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from authapp.models import ValAuth


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                print('LOGIN OK')
                return HttpResponseRedirect(reverse('mainapp:index'))

    form = UserLoginForm()
    context = {
        'form': form
        # 'year': date.year,
        # 'device': device,
    }
    return render(request, 'authapp/login.html', context)


def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user.send_verify_mail():
                print('Сообщение подтверждения отправленно')
            else:
                print('Ошибка отправки сообщения')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form
        # 'year': date.year,
        # 'device': device,
    }
    return render(request, 'authapp/register.html', context)

@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:login'))

@login_required()
def profile(request):
    if request.method == 'POST':
        print('POST')
        form = UserProfileForm(request.POST, request.FILES,
                                  instance=request.user)
        if form.is_valid():
            print('Form valid')
            form.save()
            # profile_form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        user_get = ValAuth.objects.get(pk=request.user.pk)
        ic(user_get)

        form = UserProfileForm(instance=request.user)


    context = {
        'form': form
        # 'year': date.year,
        # 'device': device,
    }
    return render(request, 'authapp/profile.html', context)

@login_required()
def profile1(request):
    form = UserProfileForm(instance=request.user)
    context = {
        'form': form
        # 'year': date.year,
        # 'device': device,
    }
    return render(request, 'authapp/profile.html', context)


def verify(request, email, activation_key):
    '''
        Верификация по email.
    '''
    try:
        # ic(email)
        # ic(activation_key)
        user = ValAuth.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            print(f'error activation user: {user}')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('mainapp:index'))
