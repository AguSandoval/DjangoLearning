from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin): 
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date info',{'fields':['pub_date']}),
    ('Pub info',{'fields':['author','country']}),
    ]

class ChoiceAdmin(admin.ModelAdmin):
   fieldsets = [
       (None, {"fields": ['question'], }),
       ('Choice details',{"fields":['choice_text','votes']}),
       ('Optional information*',{"fields":["author","country"],'classes':['collapse']}),
   ]
   
    

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
