from django.contrib import admin
from django.utils.html import format_html

from .models import Forum, Model

UPLOAD_URL = 'http://185.233.187.109:8000/'


@admin.register(Forum)
class ForumAdminView(admin.ModelAdmin):
    list_display = ("image_tag", "title", "started_at")
    readonly_fields = ("deleted_at",)
    fields = ("title", "description", "started_at", "ended_at", "map_urls", "logo_url", "image_urls")

    def save_model(self, request, obj: Forum, form, change):
        super().save_model(request, obj, form, change)
        if not obj.logo_url.url.startswith(UPLOAD_URL):
            obj.logo_url = UPLOAD_URL + obj.logo_url.url.removeprefix('/')

        obj.save()

    def image_tag(self, obj: Forum):
        return format_html(f'<img src="{obj.logo_url}" style="max-width:200px; max-height:200px"/>')


@admin.register(Model)
class ModelAdminView(admin.ModelAdmin):
    list_display = ("image_tag", "title", "forum", "created_at", "code", "qr_code")
    readonly_fields = (
        "created_at",
        "deleted_at",
        "count_views",
        "count_likes",
    )
    fields = (
        "logo_url",
        "value_url",
        "forum",
        "title",
        "code",
    )

    def save_model(self, request, obj: Model, form, change):
        super().save_model(request, obj, form, change)
        if not obj.logo_url.url.startswith(UPLOAD_URL):
            obj.logo_url = UPLOAD_URL + obj.logo_url.url.removeprefix('/')

        if not obj.value_url.url.startswith(UPLOAD_URL):
            obj.value_url = UPLOAD_URL + obj.value_url.url.removeprefix('/')

        obj.save()

    def qr_code(self, obj: Model):
        return format_html(
            f'<img id="barcode" src="https://api.qrserver.com/v1/create-qr-code/?data={obj.code}" alt="" title="{obj.code}" width="150" height="150"/>'
        )

    def image_tag(self, obj: Model):
        return format_html(f'<img src="{obj.logo_url}" style="max-width:200px; max-height:200px"/>')
