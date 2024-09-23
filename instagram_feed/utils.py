import instaloader
import requests
from django.core.files.base import ContentFile
from pathlib import Path
from urllib.parse import urlparse
from .models import InstagramAccount, InstagramPost


def scrape_instagram_account(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    account, created = InstagramAccount.objects.get_or_create(username=username)

    for post in profile.get_posts():
        # Descargar la imagen o video
        image_response = requests.get(post.url)
        image_name = Path(urlparse(post.url).path).name

        insta_post = InstagramPost.objects.create(
            account=account,
            post_id=post.shortcode,
            description=post.caption,
            timestamp=post.date
        )

        # Guardar la imagen
        insta_post.image_url.save(image_name, ContentFile(image_response.content))

        # Si es un video, descargar el video y guardarlo
        if post.is_video:
            video_response = requests.get(post.video_url)
            video_name = Path(urlparse(post.video_url).path).name
            insta_post.video.save(video_name, ContentFile(video_response.content))

        if InstagramPost.objects.filter(account=account).count() >= 2:
            break
