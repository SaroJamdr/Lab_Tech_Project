from rest_framework import serializers

class RevenueChartSerializer(serializers.Serializer):
    Date = serializers.ListField(child=serializers.CharField())
    values = serializers.ListField(child=serializers.FloatField())