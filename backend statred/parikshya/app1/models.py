from django.db import models
from django.db.models import TextField


class Course(models.Model):
    title = models.CharField(max_length=100, default=0)
    Course_Name = models.CharField(max_length=100)
    question_sets = models.IntegerField(default=0)
    Course_price = models.IntegerField(default=0)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos', default='default')
    Course_detail = TextField(null=True)

    def __str__(self):
        return self.title


class MainCourses(models.Model):
    Course_Name = models.CharField(max_length=100)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos', default='default')
    courses = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='main_course')
