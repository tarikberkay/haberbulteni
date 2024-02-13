from django.contrib import admin
from haberler.models import Article, Writer


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )


class WriterAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Writer, WriterAdmin)
