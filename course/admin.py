from django.contrib import admin
from .models import Course, Group, GroupMember

# Register your models here.
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(GroupMember)
