from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse

from finance.models import Company, StockHistory


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.landing_url = reverse('finance:index')
        self.stock_history_list_url = reverse('finance:stock_history_list')
        self.stock_history_detail_url = reverse('finance:stock_history_detail', args=[1])
        self.stock_history_list_api = reverse('finance:stock_api_list')

        self.company = Company.objects.create(
            name='MYCMP',
            symbol='MYCMP',
        )

        self.stock_history = StockHistory.objects.bulk_create([
            StockHistory(
                open=1.1,
                company_symbol=self.company,
                date=datetime.strptime("2021-04-04", "%Y-%m-%d"),
                high=1.2,
                low=1.0,
                close=1.1,
                adj_close=1.1,
                volume=55,
                unadjusted_volume=56,
                change=1,
                change_percent=1,
                vwap=1,
                label=1,
                change_over_time=1,
            ),
            StockHistory(
                open=1.1,
                company_symbol=self.company,
                date=datetime.strptime("2021-04-05", "%Y-%m-%d"),
                high=1.2,
                low=1.0,
                close=1.1,
                adj_close=1.1,
                volume=55,
                unadjusted_volume=56,
                change=1,
                change_percent=1,
                vwap=1,
                label=1,
                change_over_time=1,
            )
        ]
        )

    def test_landing_view(self):
        response = self.client.get(self.landing_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_stock_list_view(self):
        response = self.client.get(self.stock_history_list_url)
        self.assertEqual(len(response.context['object_list']), 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stockhistory_list.html")

    def test_stock_detail_view(self):
        response = self.client.get(self.stock_history_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['object'], StockHistory)
        self.assertTemplateUsed(response, "stock_detail.html")

    def test_stock_detail_not_found_view(self):
        self.stock_history_detail_url = reverse('finance:stock_history_detail', args=[100])
        response = self.client.get(self.stock_history_detail_url)
        self.assertEqual(response.status_code, 404)

    def test_stock_list_api_view(self):
        response = self.client.get(self.stock_history_list_api)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(response['content-type'], 'application/json')
