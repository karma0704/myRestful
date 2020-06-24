from rest_app01.serializer.serializer import SchoolSerializer
from rest_app01.models.school import School
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

"""
rest_framework开发接口v1.1.0版本
主要优化：
    通过引入rest_framework.mixins混合视图组件，将get、post方法中对于数据的处理过程进行封装；
    继承该类视图，传递数据和序列化组件参数即可

"""


class SchoolListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # queryset类型的数据集
    queryset = School.objects.all()
    # queryset类型数据序列化成
    serializer_class = SchoolSerializer

    def get(self, request, *args, **kwargs):
        """
        查询学校列表接口
        """
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        新增学校接口
        """
        return self.create(self, request, *args, **kwargs)


         
class SchoolDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    # queryset类型的数据集
    queryset = School.objects.all()
    # queryset类型数据序列化
    serializer_class = SchoolSerializer

    def get(self, request, *args, **kwargs):
        """
        查询指定学校列表接口
        """
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        修改指定学校信息接口
        """
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        """
        删除指定学校信息接口
        """
        return self.destory(self, request, *args, **kwargs)