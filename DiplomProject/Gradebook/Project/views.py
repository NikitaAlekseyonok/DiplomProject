from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import *


def is_member(user):
    if user.groups.filter(name='HeadTeacher').exists():
        return 'HeadTeacher'
    elif user.groups.filter(name='Teacher').exists():
        return 'Teacher'
    elif user.groups.filter(name='Student').exists():
        return 'Student'


def startPage(request):
    if request.user.is_authenticated:
        if is_member(request.user) == 'HeadTeacher':
            return redirect('headTeacherPage')
        if is_member(request.user) == 'Teacher':
            return redirect('')
        if is_member(request.user) == 'Student':
            return redirect('')
    else:
        return redirect('login')


def headTeacherHomePage(request):
    context = {
        'title': 'Страница завуча'
    }
    return render(request, template_name='Project/headTeacherHomePage.html', context=context)


def studentPage(request):
    context = {
        'title': 'Страница студента'
    }
    return render(request, template_name='Project/studentPage.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if is_member(request.user) == 'HeadTeacher':
                return redirect('headTeacherPage')
            if is_member(request.user) == 'Teacher':
                return redirect('')
            if is_member(request.user) == 'Student':
                return redirect('')
    else:
        form = UserLoginForm()
    return render(request, 'Project/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
