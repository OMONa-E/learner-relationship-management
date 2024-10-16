from django.contrib import admin
from .models import User, Order, OrderDetail, Trainer, Learner, Course, Activity


# Register your models.
admin.site.register( (User, Order, OrderDetail, Trainer, Learner, Course, Activity) )