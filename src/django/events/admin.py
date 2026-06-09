"""
Here we can add controls to the django admin page to manage the models we create.

Main attributes:
- list_display: what gets displayed in the rows of the models
- list_filter: what we can filter the models by
- search_fields: what fields get used when searching the models
"""
from django.contrib import admin

from .models import Comment, Event



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = (
    "title", "date", "time", "location", "author", "created_at"
  )
  list_filter = ("date", "author")
  search_fields = ("title", "location", "description")
  date_hierarchy = "date"
  ordering = ("date", "time")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("event", "author", "created_at")
  list_filter = ("created_at",)
  search_fields = ("body",)
