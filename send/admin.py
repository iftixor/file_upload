from django.contrib import admin
from .models import Upload, UploadImage


class UploadImageInline(admin.StackedInline):
    model = UploadImage


class UploadAdmin(admin.ModelAdmin):
    inlines = [
        UploadImageInline,
    ]


admin.site.register(Upload, UploadAdmin)