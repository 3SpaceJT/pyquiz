from django.contrib import admin

from pyquiz.quiz.models import Question, Answer, Quiz

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
