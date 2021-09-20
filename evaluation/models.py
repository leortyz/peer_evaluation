from course.models import Course
from django.db import models
from decouple import config
from course.models import Course, Group
from student.models import Student
# Create your models here.


class Evaluation(models.Model):
    name=models.CharField(max_length=1000, default=config('DEFAULT_EVALUATION_NAME'))
    enable= models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        evaluation = list(Evaluation.objects.filter(enable=True))
        if len(evaluation)==0:
            super(Evaluation, self).save(*args, **kwargs)
        else:
            self.enable=False
            super(Evaluation, self).save(*args, **kwargs)


class EvaluationStudent(models.Model):
    grader=models.ForeignKey(Student, related_name = 'student_grader',on_delete=models.CASCADE, blank=True, null=True)
    graded=models.ForeignKey(Student, related_name = 'student_graded', on_delete=models.CASCADE, blank=True, null=True)
    grade=models.PositiveIntegerField()
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.pk)