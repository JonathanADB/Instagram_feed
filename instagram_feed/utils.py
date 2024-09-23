import instaloader
import requests
from django.core.files.base import ContentFile
from pathlib import Path
from urllib.parse import urlparse
from .models import InstagramAccount, InstagramPost, InstagramMedia

def scrape_instagram_account(username):
    L = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(L.context, username)
    account, created = InstagramAccount.objects.get_or_create(username=username)

    for post in profile.get_posts():
        insta_post, created = InstagramPost.objects.get_or_create(
            account=account,
            post_id=post.shortcode,
            defaults={
                'description': post.caption,
                'timestamp': post.date
            }
        )
        if post.typename == 'GraphImage':
            download_media(post.url, insta_post, 'image')
        elif post.typename == 'GraphVideo':
            download_media(post.video_url, insta_post, 'video')
        elif post.typename == 'GraphSidecar':
            for media in post.get_sidecar_nodes():
                if media.is_video:
                    download_media(media.video_url, insta_post, 'video')
                else:
                    download_media(media.display_url, insta_post, 'image')

        if InstagramPost.objects.filter(account=account).count() >= 3:
            break

def download_media(media_url, insta_post, media_type):
    media_response = requests.get(media_url)
    media_name = Path(urlparse(media_url).path).name
    InstagramMedia.objects.create(
        post=insta_post,
        media_type=media_type,
        media_url=ContentFile(media_response.content, name=media_name)
    )
