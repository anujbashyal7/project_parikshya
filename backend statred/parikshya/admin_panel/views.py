from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app1.models import Course
from .forms import LoginForm, EditCourse


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
    add_course_query = Course.objects.all()
    form = EditCourse(request.POST)
    context = {'add_course_query': add_course_query, 'form': form}
    return render(request, 'admin_panel/add_course.html', context)


def add_course_post(request, ):
    if request.method == 'POST':
        form = EditCourse(request.POST, request.FILES)
        if form.is_valid():
            Course_Name = form.cleaned_data.get('Course_Name')
            question_sets = form.cleaned_data.get('question_sets')
            Course_price = form.cleaned_data.get('Course_price')
            photo_img = form.cleaned_data.get('photo_img')
            print(photo_img)
            Course_detail = form.cleaned_data.get('Course_detail')
            add_course_query = Course.objects.create(Course_Name=Course_Name, question_sets=question_sets,
                                                     Course_price=Course_price,
                                                     Course_detail=Course_detail,
                                                     photo_img=photo_img)

            add_course_query.save()
            return redirect('course_page')
        else:
            print(form.errors)


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
