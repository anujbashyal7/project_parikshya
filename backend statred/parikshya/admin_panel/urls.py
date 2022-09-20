from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='ap_index'),
    path('admin_signup_post/', views.admin_signup_post, name='admin_signup_post'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('course_page/', views.course_page, name='course_page'),
    path('question_page/', views.question_page, name='question_page'),
    path('student_page/', views.student_page, name='student_page'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/', views.edit_course, name='edit_course'),
    path('question_list/', views.question_list, name='question_list'),
    path('add_question/', views.add_question, name='add_question'),
    path('edit_question/', views.edit_question, name='edit_question'),
    path('view_marks/', views.view_marks, name='view_marks'),
]
