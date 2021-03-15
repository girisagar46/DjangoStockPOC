import django_filters

from .models import StockHistory


class StockFilter(django_filters.FilterSet):
    strict = False

    class Meta:
        model = StockHistory
        fields = ("company_symbol", "date")
