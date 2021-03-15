import json
import os
from datetime import datetime

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from finance.models import Company, StockHistory


class Command(BaseCommand):
    """Temporary Script to Initialize Data"""

    def add_arguments(self, parser):
        parser.add_argument('-l', '--local', type=bool, help='Load the data from online or offline?')

    def save_to_db(self, historical_stock_list):
        for historical_stock in historical_stock_list:
            company_symbol = historical_stock.get("symbol")
            company, _ = Company.objects.get_or_create(name=company_symbol, symbol=company_symbol)
            for each in historical_stock.get("historical"):
                sh = StockHistory.objects.create(
                    open=each.get("open"),
                    company_symbol=company,
                    date=datetime.strptime(each.get("date"), "%Y-%m-%d"),
                    high=each.get("high"),
                    low=each.get("low"),
                    close=each.get("close"),
                    adj_close=each.get("adjClose"),
                    volume=each.get("volume"),
                    unadjusted_volume=each.get("unadjustedVolume"),
                    change=each.get("change"),
                    change_percent=each.get("changePercent"),
                    vwap=each.get("vwap"),
                    label=each.get("label"),
                    change_over_time=each.get("changeOverTime"),
                )
                sh.save()

    def get_from_online(self):
        FMP_API_KEY = os.environ.get("FMP_API_KEY")
        API_URL = f"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOGL,AMZN?apikey={FMP_API_KEY}"
        response = requests.get(API_URL)
        historical_stock_list = response.json()
        self.save_to_db(historical_stock_list)

    def handle(self, *args, **options):
        local = options['local']
        if local:
            with open(f'{settings.BASE_DIR}/data/offline.json') as f:
                historical_stock_list = json.load(f)
                self.save_to_db(historical_stock_list.get("historicalStockList"))
        else:
            self.get_from_online()
