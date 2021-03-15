from rest_framework import serializers

from finance.models import StockHistory


class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = '__all__'
