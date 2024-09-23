from django.contrib import admin
from .models import InstagramAccount, InstagramPost
from .utils import scrape_instagram_account


@admin.register(InstagramAccount)
class InstagramAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_updated')
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        scrape_instagram_account(obj.username)


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('account', 'post_id', 'timestamp')
    list_filter = ('account',)
    search_fields = ('post_id',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('account')


