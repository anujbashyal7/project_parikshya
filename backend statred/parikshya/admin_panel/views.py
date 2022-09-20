from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm


def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'admin_panel/login_page.html', context)


def admin_signup_post(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_page')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('ap_index')


def dashboard_page(request):
    return render(request, 'admin_panel/dashboard.html')


def course_page(request):
    return render(request, 'admin_panel/course.html')


def question_page(request):
    return render(request, 'admin_panel/questions.html')


def student_page(request):
    return render(request, 'admin_panel/student.html')


def add_course(request):
    return render(request, 'admin_panel/add_course.html')


def edit_course(request):
    return render(request, 'admin_panel/edit_course.html')


def question_list(request):
    return render(request, 'admin_panel/question_list.html')


def add_question(request):
    return render(request, 'admin_panel/add_question.html')


def edit_question(request):
    return render(request, 'admin_panel/edit_question.html')


def view_marks(request):
    return render(request, 'admin_panel/view_marks.html')
