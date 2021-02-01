from django.contrib import admin
from polls_app.models import *
import nested_admin


class QuestionPointInline(nested_admin.NestedStackedInline):
    model = QuestionPoint


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [QuestionPointInline]


class PollAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionPointInline]


class QuestionPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'question')
    fields = ('name', 'question')


class UserQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionPoint, QuestionPointAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)
