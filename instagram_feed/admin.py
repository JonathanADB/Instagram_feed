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
    list_display = ('username', 'last_updated', 'profile_picture_preview')
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        scrape_instagram_account(obj.username)

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_picture.url)
        return ""
    profile_picture_preview.short_description = 'Profile Picture'
