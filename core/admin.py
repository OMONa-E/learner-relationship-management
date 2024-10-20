from django.contrib import admin
from .models import User, Order, Trainer, Learner, Course, Activity, Department, Enrollment


# Register your models.
admin.site.register( (User, Order, Trainer, Learner, Course, Activity, Department, Enrollment) )