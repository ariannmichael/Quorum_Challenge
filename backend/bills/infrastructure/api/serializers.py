from rest_framework import serializers

class BillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    primary_sponsor = serializers.IntegerField()


class BillAnalyticsSerializer(serializers.Serializer):
    bill = BillSerializer()
    supporters = serializers.IntegerField()
    opposers = serializers.IntegerField()