from django.db import models
class registration(models.Model):
    name=models.CharField(max_length=20,default="")
    email=models.CharField(max_length=30,default="")
    mobile=models.CharField(max_length=20,default="")
    username=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=40,default="")
    gender=models.CharField(max_length=10,default="")
    type_user=models.CharField(max_length=10,default="")


    def __str__(self):
        return self.username
