from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mock_test', views.mock_test_page, name='mock_test_page'),
]