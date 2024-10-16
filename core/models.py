from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# User model
class User(AbstractUser):
    nin = models.CharField(max_length=25)
    date_of_birth = models.DateField(default=datetime.now)
    phone = models.IntegerField(default=256700000000)
    address = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='static/media/profile_images/% Y/% m/% d/', blank=True, null=True)
    document = models.FileField(upload_to='static/media/documents/% Y/%m/% d', blank=True, null=True)


# Trainer model
class Trainer(models.Model):
    POSITIONS = (
        ('Entry', 'Entry'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Principal', 'Principal')
    )
    DEPT = (
        ('Mechanical', 'Mechanical'),
        ('Electrical', 'Electrical'),
        ('Robotic', 'Robotic'),
        ('Computer', 'Computer')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    positon = models.CharField(max_length=20, choices=POSITIONS)
    department = models.CharField(max_length=20, choices=DEPT)
    hired_date = models.DateField(default=datetime.now)
    salary = models.FloatField(default=0.0)


# Learner model
class Learner(models.Model):
    GROUP = (
        ('Starter', 'Starter'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(choices=GROUP, default=None, blank=True, null=True, max_length=20)
    is_phoned = models.BooleanField(default=False)
    is_emailed = models.BooleanField(default=False)


# Learner model
class Activity(models.Model):
    TYPE = (
        ('Personal', 'Personal'),
        ('Business', 'Business'),
        ('Finance', 'Finance'),
        ('Sale', 'Sale'),
        ('Learning', 'Learning'),
        ('Login', 'Login'),
        ('Logout', 'Logout')
    )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=TYPE)
    description = models.TextField(null=True, blank=True, max_length=255)
    date_took_place = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0)


# Course model
class Course(models.Model):
    DEPT = (
        ('Mechanical', 'Mechanical'),
        ('Electrical', 'Electrical'),
        ('Robotic', 'Robotic'),
        ('Computer', 'Computer')
    )
    RESTRICT = (
        ('Starter', 'Starter'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance')
    )
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    duration = models.IntegerField(default=0)
    category = models.CharField(choices=DEPT, default=None, max_length=10)
    price = models.FloatField(default=0.0)
    restriction = models.CharField(choices=RESTRICT, default=None, max_length=20)


# OrderDetail model
class OrderDetail(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0.0)
    unit_price = models.FloatField(default=0.0)


# Order model
class Order(models.Model):
    PAY_METHOD = (
        ('Bank', 'Bank'),
        ('MobileMoney', 'MobileMoney'),
        ('AirtelMoney', 'AirtelMoney'),
        ('PayPal', 'PayPal'),
        ('VisaCard', 'VisaCard')
    )
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.now)
    total_amount = models.FloatField(default=0.0)
    payment_method = models.CharField(choices=PAY_METHOD, max_length=20, default=None)
