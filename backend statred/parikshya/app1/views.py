from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from numpy.ma import ids

from .forms import CreateUserForm
from app1.models import Course


def index(request):
    course_query = Course.objects.all()
    print(course_query, '......')
    context = {'course_query': course_query}
    return render(request, 'client/index.php', context)


def mock_test_page(request):
    course_query = Course.objects.all()
    context = {'course_query': course_query}
    return render(request, 'mocktest.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('mock_test_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mock_test_page')
            else:
                messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login_and_register/login.html')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('mock_test_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login_page')
        context = {'form': form}
    return render(request, 'login_and_register/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page')


def per_category_page(request):
    return render(request, 'per_cat_available_test.html')


def test_page(request):
    return render(request, 'Per_test_page.html')


def questions_page(request):
    return render(request, 'question1.html')
