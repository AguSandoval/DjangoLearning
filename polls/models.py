from django.db import models
import datetime
from django.utils import timezone
from django_countries.fields import CountryField

class Question(models.Model): 
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    country = CountryField()
    def __str__(self):
        return self.question_text
        return self.author
        return self.country
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.PROTECT) 
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    country = CountryField()
    def __str__(self):
        return self.choice_text
        return self.author
        return self.country







