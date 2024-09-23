from django.db import models

class InstagramAccount(models.Model):
    username = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username

class InstagramPost(models.Model):
    account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='instagram_images/',null=True, blank=True)
    video_url = models.FileField(upload_to='instagram_videos/',null=True, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField()


