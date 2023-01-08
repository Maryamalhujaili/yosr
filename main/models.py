from django.db import models

# Create your models here.
class Grade(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title + " - " + self.grade.title

class File(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title