from django.contrib import admin

from .models import Evaluation, EvaluationStudent

# Register your models here.
admin.site.register(Evaluation)
admin.site.register(EvaluationStudent)
