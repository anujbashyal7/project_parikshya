from django.shortcuts import render
from numpy.ma import ids

from app1.models import Course


def index(request):
    course_query = Course.objects.all()
    print(course_query, '......')
    context = {'course_query': course_query}
    return render(request, 'index.php', context)


def mock_test_page(request):
    course_query = Course.objects.all()
    context = {'course_query': course_query}
    return render(request, 'mock.php', context)
