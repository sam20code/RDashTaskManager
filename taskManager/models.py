from django.db import models

# Create your models here.
class Sprint(models.Model):
    def __str__(self):
        return self.sprintName
    sprintName = models.CharField(max_length=200,primary_key=True)
    sprintCreatedBy = models.CharField(max_length=200)
    sprintDataPoints = models.IntegerField()
    sprintDate = models.DateTimeField()

class Task(models.Model):
    def __str__(self):
        return self.taskName
    taskName = models.TextField(max_length=5000,primary_key=True)
    taskDescription = models.CharField(max_length=5000)
    taskAssignee = models.CharField(max_length=1000)
    taskPoints = models.IntegerField()
    taskState = models.CharField(max_length=1000)
    sprintName = models.ForeignKey(Sprint, to_field='sprintName',on_delete=models.CASCADE)