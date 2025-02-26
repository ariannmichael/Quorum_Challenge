from rest_framework import serializers

class BillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    primary_sponsor = serializers.IntegerField()


class BillStatsSerializer(serializers.Serializer):
    bill = BillSerializer()
    supporters = serializers.IntegerField()
    opposers = serializers.IntegerField()
    primary_sponsor = serializers.IntegerField()