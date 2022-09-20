from django.db import models


class Course(models.Model):
    Course_Name = models.CharField(max_length=100)
    Course_price = models.IntegerField(default=0)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos', default='default')


class Student(models.Model):
    class Meta:
        db_table = 'student'

    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
