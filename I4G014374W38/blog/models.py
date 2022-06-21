from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_date = models.DateTimeField(timezone.now)
    pub_date = models.DateTimeField(auto_now_add=True)