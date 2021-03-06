from django.db import models
import datetime
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
class blog(models.Model):
    title=models.CharField(max_length=200,default="")
    language=models.CharField(max_length=20,default="")
    description=models.CharField(max_length=500,default="")
    main=models.CharField(max_length=1000,default="")
    code=models.CharField(max_length=300,default="")
    output=models.CharField(max_length=300,default="")
    date=models.CharField(max_length=10,default="/".join(str(datetime.datetime.now()).split(" ")[0].split("-")[::-1]))
    writer_name=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.title
class writer(models.Model):
    name1=models.CharField(max_length=20,default="")
    email1=models.CharField(max_length=30,default="")
    mobile1=models.CharField(max_length=20,default="")
    username1=models.CharField(max_length=30,default="")
    password1=models.CharField(max_length=40,default="")
    gender1=models.CharField(max_length=10,default="")
    type_user1=models.CharField(max_length=10,default="")

    def __str__(self):
        return self.username1
