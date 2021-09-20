from django.contrib import admin

from .models import Evaluation, EvaluationCourse, EvaluationStudent

# Register your models here.
admin.site.register(Evaluation)
admin.site.register(EvaluationCourse)
admin.site.register(EvaluationStudent)
