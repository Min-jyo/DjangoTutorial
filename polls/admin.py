from django.contrib import admin

# Register your models here.
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
