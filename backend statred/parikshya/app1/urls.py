from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mock_test', views.mock_test_page, name='mock_test_page'),
    path('login', views.login_page, name='login_page'),
    path('registration', views.registration_page, name='registration_page'),
]
