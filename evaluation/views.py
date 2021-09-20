from django.core.checks import messages
from evaluation.models import Evaluation, EvaluationStudent
from django.shortcuts import render
from decouple import config
from django.http import HttpResponse
from student.models import Student
from course.models import GroupMember, Group

def index(request):
    return render(request, 'index.html',{"course":config('DEFAULT_COURSE_NAME')})

def loaddata(request):  
    message=config('COMPLETION_MESSAGE')   
    if request.method == "GET":        
        enrollment=request.GET.get("enrollment",None) 
        grader=Student.objects.get(enrollment=enrollment)
        groupmember = GroupMember.objects.get(student=grader)
        members = GroupMember.objects.filter(group=groupmember.group)
        members = members.exclude(student=grader)
        for m in members:
            evaluation=list(EvaluationStudent.objects.filter(grader=grader,graded=m.student))
            if evaluation!=[]:
                members=members.exclude(student=m.student)
        if len(members)>0:
            response={
                "course":config('DEFAULT_COURSE_NAME'),
                "student":grader,
                "group":groupmember.group,
                "members": members
            }
            return render(request, 'evaluation.html',response)
        else:
            evaluations=EvaluationStudent.objects.filter(graded=grader)
            grade_grade=0
            if len(evaluations)>0:
                for e in evaluations:
                    grade_grade+=e.grade
                grade_grade=grade_grade/len(evaluations)
            response={
                "course":config('DEFAULT_COURSE_NAME'),            
                "student":grader,
                "message": message,
                "grade": grade_grade
            }
            return render(request, 'completed.html',response)
    else:      
        tmp=dict(request.POST)        
        l_graded=tmp["graded"]
        l_grade=tmp["grade"]
        l_grader=tmp["grader"]
        grader=Student.objects.get(pk=l_grader[0])
        for graded,grade in zip(l_graded,l_grade):
            graded=Student.objects.get(pk=graded)
            try:
                evaluation=EvaluationStudent(grader=grader, graded=graded,grade=grade)
                evaluation.save()
            except:
                message= "try again"
        evaluations=EvaluationStudent.objects.filter(graded=grader)
        grade_grade=0
        if len(evaluations)>0:
            for e in evaluations:
                grade_grade+=e.grade
            grade_grade=grade_grade/len(evaluations)
        response={
            "course":config('DEFAULT_COURSE_NAME'),            
            "student":grader,
            "message": message,
            "grade": grade_grade
        }
        return render(request, 'completed.html',response)



