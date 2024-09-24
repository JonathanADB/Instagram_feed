from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import magic  #librería para la validación de MIME types.


class InstagramAccount(models.Model):
    username = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username

class InstagramPost(models.Model):
    account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account.username} - {self.post_id}"

    def get_image_urls(self):
        return [media.media_url.url for media in self.media.filter(media_type='image')]

    def get_video_urls(self):
        return [media.media_url.url for media in self.media.filter(media_type='video')]

class InstagramMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    post = models.ForeignKey(InstagramPost, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    media_url = models.FileField(upload_to='instagram_media/')

    def __str__(self):
        return f"Media ({self.media_type}) for post {self.post.post_id}"

    def clean(self):
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_buffer(self.media_url.open().read())
        self.media_url.close()

        valid_image_mime_types = ['image/jpeg', 'image/png', 'image/jpg']
        valid_video_mime_types = ['video/mp4', 'video/quicktime']

        if self.media_type == 'image' and file_mime_type not in valid_image_mime_types:
            raise ValidationError(
                f"Invalid file type for image. Supported types are: {', '.join(valid_image_mime_types)}")

        if self.media_type == 'video' and file_mime_type not in valid_video_mime_types:
            raise ValidationError(
                f"Invalid file type for video. Supported types are: {', '.join(valid_video_mime_types)}")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


