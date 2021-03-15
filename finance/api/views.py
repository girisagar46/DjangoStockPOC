from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from finance.models import StockHistory
from finance.serializers import StockHistorySerializer


# https://www.django-rest-framework.org/api-guide/pagination/
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 150


class CompanyHistoryListAPIView(generics.ListAPIView):
    queryset = StockHistory.objects.order_by('-date')
    serializer_class = StockHistorySerializer
    pagination_class = StandardResultsSetPagination
