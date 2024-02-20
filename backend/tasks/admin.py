from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created")
    list_display_links = ("title",)
    search_fields = ("title", "description")


admin.site.register(Task, TaskAdmin)