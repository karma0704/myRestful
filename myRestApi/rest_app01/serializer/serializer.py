from rest_framework.serializers import Serializer, ModelSerializer
from rest_app01.models.school import School


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
