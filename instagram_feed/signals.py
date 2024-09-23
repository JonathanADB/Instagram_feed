# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.cache import cache
# import instaloader
# import logging
# from .models import InstagramAccount
#
# logger = logging.getLogger(__name__)
#
# @receiver(post_save, sender=InstagramAccount)
# def fetch_instagram_data(sender, instance, created, **kwargs):
#     if created:
#         loader = instaloader.Instaloader()
#
#         try:
#             # Intentamos cargar los datos de Instagram
#             profile = instaloader.Profile.from_username(loader.context, instance.username)
#             instance.profile_picture = profile.profile_pic_url
#             instance.bio = profile.biography
#
#             # Obtener los últimos 2 posts de manera optimizada
#             posts_data = []
#             for post in profile.get_posts().limit(2):  # Usar limit=2
#                 post_info = {
#                     'post_image': post.url,
#                     'description': post.caption,
#                     'created_at': post.date_utc.isoformat(),
#                 }
#                 posts_data.append(post_info)
#
#             instance.posts = posts_data
#             instance.save()
#
#         except instaloader.exceptions.ProfileNotExistsException:
#             logger.error(f"No existe la cuenta de Instagram: {instance.username}")
#         except instaloader.exceptions.ConnectionException:
#             logger.error(f"Error de conexión al intentar obtener el perfil de {instance.username}")
#         except Exception as e:
#             logger.error(f"Error inesperado al obtener el perfil de {instance.username}: {str(e)}")
#
#
