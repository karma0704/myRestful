from rest_app01.serializer.serializer import SchoolSerializer
from rest_app01.models.school import School
from rest_framework.viewsets import ModelViewSet


"""
rest_framework开发接口v1.2.0版本
主要优化：


"""


class SchoolViewSet(ModelViewSet):
    # queryset类型的数据集
    queryset = School.objects.all()
    # queryset类型数据序列化成
    serializer_class = SchoolSerializer