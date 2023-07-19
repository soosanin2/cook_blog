from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipleInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


# налаштування адмінки
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "create_at", "author"]
    inlines = [RecipleInline]
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)