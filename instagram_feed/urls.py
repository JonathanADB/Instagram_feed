from django.urls import path
from .views import account_list


urlpatterns = [
    path('get_posts/', account_list, name='acount-list'),

]