from rest_framework import serializers

from .models import Upload, UploadImage

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('image',)


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='MyUser')
    images = UploadImageSerializer(source='uploadimage_set', many=True, read_only=True)

    class Meta:
        model = Upload
        fields = ('id', 'title', 'user', 'timestamp', 'images',)

    def create(self, validated_data):
        request_user = self.context.get('view').request.user
        user = User.objects.get(pk=request_user.id)
        images_data = self.context.get('view').request.FILES
        upload = Upload.objects.create(title=validated_data.get('title', 'no-title'),
                                       user_id=user.id)
        title = upload.title
        company_name = user.company_name

        message = " "
        for image_data in images_data.values():
            uploaded_image = UploadImage.objects.create(upload=upload, image=image_data)
            print(uploaded_image)
            message = message + "\nNew image url  " + self.context['request'].build_absolute_uri(
                uploaded_image.image.url) + "  ,  "

        subject = "{}, {}, {}, {}".format(company_name, user.email, user.get_full_name(), title)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['iftixor.rajabov@gmail.com']
        email = send_mail(subject, message, email_from, recipient_list)
        print(email)
        print(company_name)
        return upload