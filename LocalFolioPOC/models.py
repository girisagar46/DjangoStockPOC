from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    symbol = models.CharField(max_length=5, null=False, unique=True, verbose_name="NASDAQ Ticker Symbol")

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.symbol


class StockHistory(models.Model):
    company_symbol = models.ForeignKey("Company", on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=False)
    open = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    close = models.FloatField(null=False)
    adj_close = models.FloatField(null=False)
    volume = models.FloatField(null=False)
    unadjusted_volume = models.FloatField(null=False)
    change = models.FloatField(null=False)
    change_percent = models.FloatField(null=False)
    vwap = models.FloatField(null=False)
    label = models.CharField(max_length=30, null=False)
    change_over_time = models.FloatField(null=False)

    class Meta:
        db_table = "stock_history"

    def __str__(self):
        return f"{self.company_symbol.symbol}: {self.date}"
