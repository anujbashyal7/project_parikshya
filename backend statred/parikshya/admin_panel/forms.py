from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from app1.models import Course


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class EditCourse(forms.ModelForm):
    photo_img = forms.ImageField(
        label='Select Image', required=False, initial='default')

    class Meta:
        model = Course
        fields = ('Course_Name','question_sets', 'Course_price', 'photo_img', 'Course_detail')
