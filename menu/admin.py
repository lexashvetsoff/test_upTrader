from django.contrib import admin

from .models import MenuCategory, TreeMenu


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]
