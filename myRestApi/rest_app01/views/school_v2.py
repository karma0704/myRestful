from rest_app01.serializer.serializer import SchoolSerializer
from rest_app01.models.school import School
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


"""
rest_framework开发接口v1.2.0版本
主要优化：
    通过使用mixin类，我们使用更少的代码重写了这些视图，但我们还可以再进一步。
    REST框架提供了一组已经混合好（mixed-in）的通用视图，我们可以使用它来简化我们的views.py模块。
    from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""


class SchoolListView(ListCreateAPIView):
    # queryset类型的数据集
    queryset = School.objects.all()
    # queryset类型数据序列化成
    serializer_class = SchoolSerializer

         
class SchoolDetailView(RetrieveUpdateDestroyAPIView):
    # queryset类型的数据集
    queryset = School.objects.all()
    # queryset类型数据序列化
    serializer_class = SchoolSerializer