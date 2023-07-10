from django.contrib import admin
from django.utils.html import format_html

from .models import Forum, Model


@admin.register(Forum)
class ForumAdminView(admin.ModelAdmin):
    list_display = ("image_tag", "title", "started_at")
    readonly_fields = ("deleted_at",)
    fields = ("title", "description", "started_at", "ended_at", "image_urls", "map_urls")

    def image_tag(self, obj: Forum):
        return format_html(f'<img src="{obj.logo_url}" style="max-width:200px; max-height:200px"/>')


@admin.register(Model)
class ModelAdminView(admin.ModelAdmin):
    list_display = ("image_tag", "title", "forum", "created_at")
    readonly_fields = (
        "created_at",
        "deleted_at",
        "count_views",
        "count_likes",
    )
    fields = (
        "logo_url",
        "value_url",
        "code",
        "forum",
        "title",
    )

    def image_tag(self, obj: Model):
        return format_html(f'<img src="{obj.logo_url}" style="max-width:200px; max-height:200px"/>')
