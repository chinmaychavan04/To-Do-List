from django.db import models

# Create your models here.

class AddMembers(models.Model):
    fullName=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    startDate=models.DateField()
    endDate=models.DateField()
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.fullName
