from django.contrib import admin
from persons.models import anonim_message
# Register your models here.
class AricleInkine(admin.StackedInline):
    model = anonim_message
    extra = 1

class AN_message(admin.ModelAdmin):
    fields = ['text_message','nickname_message']
    inlines = [AricleInkine]

admin.site.register(anonim_message)