from rest_framework import serializers


class LegislatorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)


class LegislatorVoteAnalyticsSerializer(serializers.Serializer):
    legislator = LegislatorSerializer()
    supported_bills = serializers.IntegerField()
    opposed_bills = serializers.IntegerField()

