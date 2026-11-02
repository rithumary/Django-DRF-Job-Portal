from rest_framework import serializers
from Jobs.models import CompanyDb,JobDb,ApplicationDb

class Comapny_serializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyDb
        fields="__all__"
        read_only_fields=["id"]
class Job_serializer(serializers.ModelSerializer):
    class Meta:
        model=JobDb
        fields="__all__"
        read_only_fields=["id"]
class Application_serializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDb
        fields = "__all__"
        read_only_fields = ["id", "applied_at"]
