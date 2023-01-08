from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Grade, Subject, File
from django.db.models import Q

def home(request):
    grades = Grade.objects.all()
    return render(request, 'home.html', {'grades': grades})

def grade_detail(request, pk):
    grade = get_object_or_404(Grade, id=pk)
    subjects = get_list_or_404(Subject, grade=grade)
    return render(request, 'grade.html', {'subjects': subjects})

def search(request):
    subjects = Subject.objects.filter(Q(title__icontains=request.POST.get('search', '')))
    return render(request, 'grade.html', {'subjects': subjects})

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, id=pk)
    files = get_list_or_404(File, subject=subject)
    return render(request, 'subject.html', {'files': files})
        

