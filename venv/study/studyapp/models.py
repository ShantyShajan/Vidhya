from django.db import models
from django.db import models
import datetime
import os
from asyncio.windows_events import NULL



class reg(models.Model):
    name = models.CharField(max_length=50,default='')
    dob = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='',unique=True)
    gender = models.CharField(max_length=50,default='') 
    mobile = models.CharField(max_length=50,default='')
    course = models.CharField(max_length=50,default='')
    qualification = models.CharField(max_length=50,default='')
    experience = models.CharField(max_length=50,default='')
    board = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    usertype = models.CharField(max_length=50,default='')


class complaints(models.Model):
    uid = models.ForeignKey(reg,on_delete=models.CASCADE,null=True)
    # uid = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    complaint = models.CharField(max_length=50,default='')
    response = models.CharField(max_length=50,default='')
    usertype = models.CharField(max_length=50,default='')

class jobs(models.Model):
    job = models.CharField(max_length=50,default='')
    institution = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')
    salary = models.CharField(max_length=50,default='') 
    description = models.CharField(max_length=50,default='')

class contacts(models.Model):
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=50,default='')

class applyjobs(models.Model):
    jobid = models.CharField(max_length=50,default='')
    uid = models.CharField(max_length=50,default='')
    name = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=50,default='')
    dob = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='') 
    gender = models.CharField(max_length=50,default='')
    mobile = models.CharField(max_length=50,default='')
    qualification = models.CharField(max_length=50,default='')
    experience = models.CharField(max_length=50,default='') 
    specialization = models.CharField(max_length=50,default='')
    year = models.CharField(max_length=50,default='')
  
class course(models.Model):
    name = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=50,default='')

class chat(models.Model):
    tid = models.CharField(max_length=50,default='')
    sid = models.ForeignKey(reg,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=50,default='')
    response = models.CharField(max_length=50,default='')
    status = models.CharField(max_length=50,default='null')

def filep(request, filename):
    return os.path.join('uploaduser/', filename)

class video(models.Model):
    date = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    classes = models.CharField(max_length=50,default='')
    video = models.FileField(upload_to=filep, null=True, blank=True)


class meet(models.Model):
    date = models.CharField(max_length=50,default='')
    time = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    classes = models.CharField(max_length=50,default='')
    link = models.CharField(max_length=50,default='')

class ttable(models.Model):
    classe = models.CharField(max_length=50,default='')
    ddate = models.CharField(max_length=50,default='')
    time = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')

class exam(models.Model):
    classe = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    date = models.CharField(max_length=50,default='')
    time = models.CharField(max_length=50,default='')
    link = models.CharField(max_length=50,default='')

def filepr(request, filename):
    return os.path.join('uploaduser/', filename)

class uploads(models.Model):
    classe = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    year= models.CharField(max_length=50,default='')
    browse = models.FileField(upload_to=filepr, null=True, blank=True)
    mtype = models.CharField(max_length=50,default='')

# Create your models here.
