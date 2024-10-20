from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# User model
class User(AbstractUser):
    nin = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.now)
    phone = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(blank=True, null=True,max_length=100)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    positon = models.CharField(max_length=20, choices=POSITIONS)    
    hired_date = models.DateField(default=datetime.now)
    salary = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'<Trainer: {self.user.username}>'


# Department model
class Department(models.Model):
    NAME = (
        ('Mechanical', 'Mechanical'),
        ('Electrical', 'Electrical'),
        ('Robotic', 'Robotic'),
        ('Computer', 'Computer')
    )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    learner = models.ForeignKey('Learner', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=NAME, default=None)
    description = models.TextField(null=True, blank=True, max_length=255)

    def __str__(self) -> str:
        return f'<Department: {self.name}>'


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

    def __str__(self) -> str:
        return f'<Learner: {self.group}>'


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
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE)
    description = models.TextField(null=True, blank=True, max_length=255)
    date_took_place = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'<Activity: {self.type}>'


# Course model
class Course(models.Model):
    RESTRICT = (
        ('Starter', 'Starter'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance')
    )
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True, max_length=255)
    duration = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    restriction = models.CharField(choices=RESTRICT, default=None, max_length=20)

    def __str__(self) -> str:
        return f'<Course: {self.name}>'


# Enrollment model
class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_executed = models.BooleanField(default=False)
    progress = models.FloatField(default=0.0)
    date_of_enrollment = models.DateTimeField(auto_now=True)
   
    
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
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0.0)
    unit_price = models.FloatField(default=0.0)
    total_amount = models.FloatField(default=0.0)
    order_date = models.DateField(default=datetime.now)
    is_checked = models.BooleanField(default=False)    
    payment_method = models.CharField(choices=PAY_METHOD, max_length=20, default='VisaCard')

    def __str__(self) -> str:
        return f'<Order: {self.course}>'
