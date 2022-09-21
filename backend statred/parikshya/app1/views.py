from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from numpy.ma import ids

from .forms import CreateUserForm
from app1.models import Course


def index(request):
    course_query = Course.objects.all()
    print(course_query, '......')
    context = {'course_query': course_query}
    return render(request, 'client/index.php', context)


@login_required(login_url='login_page')
def mock_test_page(request):
    course_query = Course.objects.all()
    context = {'course_query': course_query}
    return render(request, 'mocktest.html', context)


def login_page(request):
    form = CreateUserForm()
    return render(request, 'login_and_register/login.html', {'form': form})


def login_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mock_test_page')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login_page')


def registration_page(request):
    form = CreateUserForm()
    return render(request, 'login_and_register/register.html', {'form': form})


def registration_post(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return redirect('registration_page')
            else:
                student_query = User.objects.create_user(username=username, password=password1, email=email)
                student_query.save()
                print('User created')
                return redirect('login_page')
        else:
            messages.error(request, "Password doesnot matched!!!")
            return redirect('registration_page')


def logout_user(request):
    logout(request)
    return redirect('login_page')


def per_category_page(request):
    return render(request, 'per_cat_available_test.html')


def test_page(request):
    return render(request, 'Per_test_page.html')


def questions_page(request):
    return render(request, 'question1.html')
