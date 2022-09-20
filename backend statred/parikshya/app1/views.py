from django.shortcuts import render
from numpy.ma import ids

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

    return render(request, 'login_and_register/login.html')


def registration_page(request):
    return render(request, 'login_and_register/register.html')


def per_category_page(request):
    return render(request, 'per_cat_available_test.html')


def test_page(request):
    return render(request, 'Per_test_page.html')


def questions_page(request):
    return render(request, 'questions.html')
