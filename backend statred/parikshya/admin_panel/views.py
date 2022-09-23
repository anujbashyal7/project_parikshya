from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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


def logout_user_admin(request):
    logout(request)
    return redirect('ap_index')


@login_required(login_url='ap_index')
def dashboard_page(request):
    return render(request, 'admin_panel/dashboard.html')


@login_required(login_url='ap_index')
def course_page(request):
    return render(request, 'admin_panel/course.html')


@login_required(login_url='ap_index')
def main_course(request):
    return render(request, 'admin_panel/main_course.html')


@login_required(login_url='ap_index')
def question_page(request):
    return render(request, 'admin_panel/questions.html')


@login_required(login_url='ap_index')
def student_page(request):
    return render(request, 'admin_panel/student.html')


@login_required(login_url='ap_index')
def add_course(request):
    return render(request, 'admin_panel/add_course.html')


@login_required(login_url='ap_index')
def edit_course(request):
    return render(request, 'admin_panel/edit_course.html')


@login_required(login_url='ap_index')
def question_list(request):
    return render(request, 'admin_panel/question_list.html')


@login_required(login_url='ap_index')
def question_set(request):
    return render(request, 'admin_panel/question_set.html')


@login_required(login_url='ap_index')
def add_question_set(request):
    return render(request, 'admin_panel/add_question_set.html')


@login_required(login_url='ap_index')
def edit_question_set(request):
    return render(request, 'admin_panel/edit_question_set.html')


@login_required(login_url='ap_index')
def add_question(request):
    return render(request, 'admin_panel/add_question.html')


@login_required(login_url='ap_index')
def edit_question(request):
    return render(request, 'admin_panel/edit_question.html')


@login_required(login_url='ap_index')
def view_marks(request):
    return render(request, 'admin_panel/view_marks.html')
