# from django.contrib import admin
# from .models import InstagramAccount, InstagramPost, InstagramImage
# from .utils import scrape_instagram_account
#
# class InstagramImageInline(admin.TabularInline):
#     model = InstagramImage
#     extra = 0
#     readonly_fields = ('image_url',)
#
# @admin.register(InstagramPost)
# class InstagramPostAdmin(admin.ModelAdmin):
#     list_display = ('account', 'post_id', 'timestamp')
#     list_filter = ('account', )
#     search_fields = ('post_id',)
#     inlines = [InstagramImageInline]
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('account').prefetch_related('images')
#
# @admin.register(InstagramAccount)
# class InstagramAccountAdmin(admin.ModelAdmin):
#     list_display = ('username', 'last_updated')
#     search_fields = ('username',)
#
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         scrape_instagram_account(obj.username)


from django.contrib import admin
from .models import InstagramAccount, InstagramPost, InstagramMedia
from .utils import scrape_instagram_account

class InstagramMediaInline(admin.TabularInline):
    model = InstagramMedia
    extra = 0
    readonly_fields = ('media_type', 'media_url')

@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('account', 'post_id', 'timestamp')
    list_filter = ('account', )
    search_fields = ('post_id',)
    inlines = [InstagramMediaInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('account').prefetch_related('media')

@admin.register(InstagramAccount)
class InstagramAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_updated')
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        scrape_instagram_account(obj.username)
