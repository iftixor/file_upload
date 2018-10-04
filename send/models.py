from django.db import models


class Upload(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('user.MyUser', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UploadImage(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    image = models.FileField()

    def __str__(self):
        return self.image.name
