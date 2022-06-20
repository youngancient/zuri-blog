from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)