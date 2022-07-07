from django.db import models
import datetime
from django.utils import timezone


from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.text
    def is_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text

