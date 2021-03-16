from rest_framework import serializers

from finance.models import StockHistory


class StockHistorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='company_symbol')

    class Meta:
        model = StockHistory
        fields = '__all__'
