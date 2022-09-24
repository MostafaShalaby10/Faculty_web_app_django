from datetime import datetime
from unicodedata import name
from xmlrpc.client import DateTime
from django.db import models

l = {("Male" , "Male") , ("Female" , "Female") , ("Other" , "Other")}

class subjects(models.Model):
    id = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=20 , null=False , blank=False)
    max_score = models.IntegerField(null=False , blank=False)
    class Meta:
        ordering  = ['id']


class tracks(models.Model):
    id = models.IntegerField(primary_key=True)
    track_name =models.CharField(max_length=20 , null=False , blank=False)
    subject_id = models.ForeignKey(subjects ,null=False , blank=False , on_delete=models.CASCADE , default=0)
    class Meta:
        ordering  = ['id']
class students(models.Model) :
    id = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=40 , null=False , blank=False)
    mail =models.CharField(max_length=40 , null=False , blank=False)
    address =models.CharField(max_length=100 , null=False , blank=False)
    phone =models.CharField(max_length=15 , null=False , blank=False)
    age = models.IntegerField(null=False , blank=False)
    gender =models.CharField(choices=l , default="other" , max_length=10)
    track_id = models.ForeignKey( tracks ,null=False , blank=False, on_delete=models.CASCADE ,default=0)
    class Meta:
        ordering  = ['id']


class exam (models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    student_id = models.ForeignKey(students  , on_delete=models.CASCADE ,null=False , blank=False,default=0)
    subject_id = models.ForeignKey(subjects  , on_delete=models.CASCADE ,null=False , blank=False,default=0 )
    class Meta:
        ordering  = ['id']
# # Create your models here.
