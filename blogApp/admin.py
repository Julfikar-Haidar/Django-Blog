from django.contrib import admin
from .models import Author, Category, Article,Comment


# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Author


admin.site.register(Author, authorModel)


class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Category


admin.site.register(Category, categoryModel)


class articleModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__", "details"]
    list_filter = ["posted_on","category"]

    class Meta:
        Model = Article


admin.site.register(Article, articleModel)


class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Comment


admin.site.register(Comment, commentModel)