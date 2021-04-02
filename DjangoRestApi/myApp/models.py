from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length = 50)
    Branch = models.CharField(max_length = 50)
    Usn_Id = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.Name
