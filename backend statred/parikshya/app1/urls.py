from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mock_test', views.mock_test_page, name='mock_test_page'),
    path('login', views.login_page, name='login_page'),
    path('login_post', views.login_post, name='login_post'),
    path('registration', views.registration_page, name='registration_page'),
    path('registration_post', views.registration_post, name='registration_post'),
    path('logout/', views.logout_user, name="logout"),
    path('per_catagory_test_page', views.per_category_page, name='per_category_page'),
    path('test_page', views.test_page, name='test_page'),
    path('questions_page', views.questions_page, name='questions_page'),
    path('purchasenow_page', views.purchasenow_page, name='purchasenow_page'),
    path('payment_options', views.payment_options, name='payment_options'),
]
