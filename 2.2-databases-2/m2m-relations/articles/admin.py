from django.contrib import admin

from .models import Article, Object, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
