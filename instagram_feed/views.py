from django.shortcuts import render
from .models import InstagramAccount


def account_list(request):
    accounts = InstagramAccount.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

