from django.db import models

class Trainee(models.Model):
    trainee = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.trainee
    
class Course(models.Model):
    course = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE, null=True)
