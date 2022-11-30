from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)