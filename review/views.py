from django.http import response
import course
from django.shortcuts import render
from decouple import config
from course.models import Course
# Create your views here.
def review(request):
    courses=Course.objects.all()
    semesters=[]
    parallels=[]
    years=[]
    for c in courses:
        if c.year not in years:
            years.append(c.year)
        if c.semester not in semesters:
            semesters.append(c.semester)
        if c.parallel not in parallels:
            parallels.append(c.parallel)
        
    response={
        "course":config('DEFAULT_COURSE_NAME'),
        "courses": courses,
        "semesters": semesters,
        "parallels": parallels,
        "years": years
    }

    return render(request, 'review.html',response)