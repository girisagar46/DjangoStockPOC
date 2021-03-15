from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    symbol = models.CharField(max_length=5, unique=True, verbose_name="NASDAQ Ticker Symbol")

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.symbol


class StockHistory(models.Model):
    company_symbol = models.ForeignKey("Company", on_delete=models.CASCADE)
    date = models.DateField(help_text="Date when the stock data was recorded.")
    open = models.FloatField(help_text="Opening price of the stock that day.")
    high = models.FloatField(help_text="High price of the stock on that day.")
    low = models.FloatField(help_text="Low price of the stock on that day.")
    close = models.FloatField(help_text="Closing price of stock that day.")
    adj_close = models.FloatField(help_text="Adjusted closing price of stock that day.")
    volume = models.FloatField(help_text="Number of shares traded in a stock")
    unadjusted_volume = models.FloatField("Unadjusted volume that day.")
    change = models.FloatField("Price difference that occurs between two points in time.")
    change_percent = models.FloatField("Change percentage in price.")
    vwap = models.FloatField(help_text="Volume Weighted Average Price")
    label = models.CharField(max_length=30, help_text="Label of the stock. Generally the date representation.")
    change_over_time = models.FloatField(help_text="Stock price change over time.")

    class Meta:
        db_table = "stock_history"

    def __str__(self):
        return f"{self.company_symbol.symbol}: {self.date}"
