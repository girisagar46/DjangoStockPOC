from django.urls import path

from LocalFolioPOC.api.views import CompanyHistoryListAPIView
from LocalFolioPOC.views import LandingView, StockHistoryListHTMLView, StockHistoryDetailHTMLView

app_name = "LocalFolioPOC"

urlpatterns = [
    path('api/list/', CompanyHistoryListAPIView.as_view()),
    path('', LandingView.as_view(), name='index'),
    path('data/', StockHistoryListHTMLView.as_view(), name='stock_history_list'),
    path('stock/<pk>/', StockHistoryDetailHTMLView.as_view(), name='stock_history_detail'),
]
