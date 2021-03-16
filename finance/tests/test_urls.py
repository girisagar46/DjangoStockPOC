from django.test import TestCase
from django.urls import resolve, reverse

from finance import views
from finance.api.views import CompanyHistoryListAPIView


class TestUrl(TestCase):

    def test_index_url_is_resolved(self):
        url = reverse('finance:index')
        self.assertEqual(resolve(url).func.view_class, views.LandingView)

    def test_api_url_is_resolved(self):
        url = reverse('finance:stock_api_list')
        self.assertEqual(resolve(url).func.view_class, CompanyHistoryListAPIView)

    def test_stock_history_list_url_is_resolved(self):
        url = reverse('finance:stock_history_list')
        self.assertEqual(resolve(url).func.view_class, views.StockHistoryListHTMLView)

    def test_stock_history_detail_url_is_resolved(self):
        url = reverse('finance:stock_history_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.StockHistoryDetailHTMLView)
