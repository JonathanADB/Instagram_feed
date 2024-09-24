from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InstagramAccount
from .serializers import InstagramAccountSerializer

@api_view(['GET'])
def account_list(request):
    accounts = InstagramAccount.objects.all()
    serializer = InstagramAccountSerializer(accounts, many=True)
    return Response(serializer.data)
