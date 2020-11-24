from django.contrib import admin

from .models import Question
from .models import Choice, Question

admin.site.register(Question)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
     list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
class ChoiceInline(admin.TabularInline):
class Question(models.Model):
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'  
