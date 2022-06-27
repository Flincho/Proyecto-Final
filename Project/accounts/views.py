import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from accounts.forms import UserRegisterForm, UserEditForm, AvatarForm
from accounts.models import Avatar


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("accounts:user-login")
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form": form},
        template_name="accounts/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome")
                return redirect("home")

        return render(
            request=request,
            context={'form': form},
            template_name="accounts/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="accounts/login.html",
    )


def logout_request(request):
    logout(request)
    return redirect("home")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('accounts:profile')

    form = UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="accounts/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('accounts:profile')

    form = AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="accounts/avatar_form.html",
    )


@login_required
def profile(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="accounts/profile.html",
    )


def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}

    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="main/home.html")


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

