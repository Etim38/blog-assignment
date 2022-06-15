from cgitb import text
from distutils.text_file import TextFile
from msilib.schema import Class
from turtle import title
from django.db import models
from django.contrib.auth.models import ForeignKey

class Post(models.Model):
 title=models.CharField(max_length=200)
 text=models.TextField()
 author =models.ForeignKey(on_delete=models.CASCADE)
 created_date =models.DateTimeField
 published_date=models.DateTimeField
