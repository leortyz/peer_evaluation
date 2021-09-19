from course.models import Course
from django.db import models
from decouple import config
from course.models import Course, Group
from student.models import Student
# Create your models here.


class Evaluation(models.Model):
    name=models.CharField(max_length=1000, default=config('DEFAULT_EVALUATION_NAME'))

    def __str__(self):
        return self.name

class EvaluationCourse(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class EvaluationStudent(models.Model):
    grader=models.ForeignKey(Student, related_name = 'student_grader',on_delete=models.CASCADE, blank=True, null=True)
    student=models.ForeignKey(Student, related_name = 'student_graded', on_delete=models.CASCADE, blank=True, null=True)
    grade=models.PositiveIntegerField()

    def __str__(self):
        return str(self.pk)
