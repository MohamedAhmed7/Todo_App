from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from todo.models import Todo
import os
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            not_completed_todo = Todo(text = 'Not completed todo example (click me to mark as done)', user_id = User.objects.filter(username = username).first())
            completed_todo = Todo(text = 'completed todo example (click me to mark as not completed)', complete = True, user_id = User.objects.filter(username = username).first())
            completed_todo.save()
            not_completed_todo.save()
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        old_username = request.user.username
        old_mail  = request.user.email
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            new_username = request.user.username
            new_mail = request.user.email
            if (new_username != old_username or new_mail != old_mail):
                u_form.save()
                # check if the user updated profile image or not to delete the old one
                messages.success(request, 'Your Account has been updated!')
            else:
                messages.warning(request, 'Nothing to be Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'users/profile.html', context)