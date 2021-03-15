from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.models import StockHistory
from finance.serializers import StockHistorySerializer


class CompanyHistoryListAPIView(APIView):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        serializer = StockHistorySerializer(StockHistory.objects.order_by('-date')[:100], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
