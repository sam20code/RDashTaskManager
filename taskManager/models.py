from django.db import models

# Create your models here.
class Sprint(models.Model):
    def __str__(self):
        return self.sprintName
    sprintName = models.CharField(max_length=200,primary_key=True)
    sprintCreatedBy = models.CharField(max_length=200)
    sprintDataPoints = models.IntegerField()
    sprintDate = models.DateTimeField()
