from django.contrib import admin
from forum.models import Article,Comments,News_up,Bany_photo,Raz_photo,Sport_zal_photo,Rooms_photo
# Register your models here.
class AricleInkine(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date']
    inlines = [AricleInkine]
    list_filter = ['article_date']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Bany_photo)
admin.site.register(Raz_photo)
admin.site.register(Sport_zal_photo)
admin.site.register(Rooms_photo)
admin.site.register(News_up)
