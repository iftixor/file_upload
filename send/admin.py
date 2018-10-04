from django.contrib import admin
from .models import Upload, UploadImage

#
# class SendFileAdmin(admin.ModelAdmin):
#     exclude = ('owner',)

admin.site.register(Upload)
admin.site.register(UploadImage)
