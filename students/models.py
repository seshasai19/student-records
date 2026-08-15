from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    student_class = models.CharField(max_length=20)
    roll_no = models.PositiveIntegerField(unique=True)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return self.name
