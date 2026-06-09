from django.contrib import admin
from .models import Vacancy, Article

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "salary", "is_active")
    search_fields = ("title", "company", "description")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)