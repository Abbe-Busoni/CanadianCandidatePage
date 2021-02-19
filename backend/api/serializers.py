from rest_framework import serializers

class CandidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500, allow_blank=True, source="Candidate Name")
    party = serializers.CharField(max_length=500, allow_blank=True, source="Party")
    riding = serializers.CharField(max_length=500, allow_blank=True, source="Riding")
    facebook_page = serializers.CharField(max_length=500, allow_blank=True, source="Facebook Page")
    twitter_handle = serializers.CharField(max_length=500, allow_blank=True, source="Twitter Handle")
    facebook_spending = serializers.IntegerField(source="Facebook Spend")
    twitter_spending = serializers.IntegerField(source="Twitter Spend")
