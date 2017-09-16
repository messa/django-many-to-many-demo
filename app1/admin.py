from django.contrib import admin

from .models import Publication, Comment, Article


class PublicationAdmin (admin.ModelAdmin):
    pass

admin.site.register(Publication, PublicationAdmin)


class CommentAdmin (admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)


class ArticleAdmin (admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
