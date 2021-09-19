from django.db import models
from decouple import config
from student.models import Student
# Create your models here.

class Course(models.Model):
    class Semester(models.TextChoices):
        PAE = '0', ('I PAE')
        PAO1 = '1', ('I PAO')
        PAO2 = '2', ('II PAO')
        NULL = '-', ('Not defined')

    class Parallel(models.TextChoices):
        ONE = '1', ('1')
        TWO = '2', ('2')
        THREE = '3', ('3')
        FOUR = '4', ('4')
        FIVE = '5', ('5')
        NULL = '-', ('Not defined')

    name=models.CharField(max_length=1000, default=config('DEFAULT_COURSE_NAME'))
    year= models.CharField(max_length=4,default=config('DEFAULT_YEAR'))
    semester = models.CharField(
        max_length=2,
        choices=Semester.choices,
        default=Semester.NULL,
    )
    parallel = models.CharField(
        max_length=2,
        choices=Parallel.choices,
        default=Parallel.NULL,
    )

    def __str__(self):
        return str(self.pk)

class Group(models.Model):
    name=models.CharField(max_length=100, default=config('DEFAULT_GROUP_NAME'))    
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    max_members = models.IntegerField(default=1)
    

    def __str__(self):
        return str(self.course) + self.name

class GroupMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.student) + str(self.group)

    def save(self, *args, **kwargs):
        members= GroupMember.objects.filter(group=self.group)
        if members.count() < self.group.max_members:
            super(GroupMember, self).save(*args, **kwargs)
        else:
            print(False)
        
