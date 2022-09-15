from django.db import models


class Course(models.Model):
    Course_Name = models.CharField(max_length=100)
    Course_price = models.IntegerField(default=0)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos', default='default')