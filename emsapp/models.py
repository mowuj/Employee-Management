
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from PIL import Image
from django.utils import timezone
from django.urls import reverse
User=get_user_model()

class Department(models.Model):
    name = models.CharField(max_length=150)
    manager=models.CharField(max_length=150,blank=True, null=True )
    start_date=models.DateField(blank=True, null=True)
    image=models.ImageField(
        default='default.jpg', upload_to='media/images', blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=150)
    salary=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, default='', blank=True, null=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,  blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, default='', blank=True, null=True, related_name='post_set')
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, default='', blank=True, null=True, related_name='district_set')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            blank=True, null=True, related_name='post_set', default='')
    employee_id = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    ssc = models.FloatField(blank=True, null=True)
    hsc = models.FloatField(blank=True, null=True)
    honors = models.FloatField(blank=True, null=True)
    masters = models.FloatField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=150, default="")
    father_name = models.CharField(max_length=150, default="")
    mother_name = models.CharField(max_length=150, default="")
    image = models.ImageField(
        default='default.jpg', upload_to='media/images', blank=True)

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return str(self.user)

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause_of_leave = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    apply_date = models.DateField(auto_now_add=True)
    check_status = models.BooleanField(default=False)
    approve_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Holiday(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    Description = models.CharField(max_length=150)

    def __str__(self):
        return str(self.Description)


class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    do_status = models.BooleanField(default=False)
    working_status = models.BooleanField(default=False)
    done_status = models.BooleanField(default=False)
    issue_date = models.DateTimeField(auto_now_add=True)
    delivery = models.DateField(
        auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.user) + " " + str(self.title)


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    person_with = models.CharField(max_length=150,blank=True, null=True)
    meeting_date = models.DateField(blank=True, null=True)
    meeting_time = models.TimeField(blank=True, null=True)
    def __str__(self):
        return str(self.user)


class Client(models.Model):
    client_name = models.CharField(max_length=150)
    client_id = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.client_name)


class Attendance(models.Model):
    attender = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.attender.username) + " " + str(self.datetime)[:19]
    
class SalesData(models.Model):
    sales=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=150)