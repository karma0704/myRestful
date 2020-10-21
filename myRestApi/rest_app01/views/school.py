from rest_app01.serializer.serializer import SchoolSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_app01.models.school import School
from django.http import HttpResponse
from authentication.user_auth import LoginAuth

"""
rest_framework开发接口v1.0.0版本
开发我们的Web API的首要任务就是为我们的Web API提供一种将代码片段实例序列化和反序列化为诸如json之类的表示形式的方式。
我们可以通过声明与django.forms非常相似的序列化组件（serializers）来实现。
导入序列化组件：from rest_app01.serializer.serializer import SchoolSerializer

"""


class SchoolListView(APIView):
    """
    局部视图认证: 再需要进行认证的类视图中添加一个变量名称为authentication_classes的视图认证类列表
    """
    authentication_classes = [LoginAuth, ]

    def get(self, request, *args, **kwargs):
        """
        查询学校列表接口
        """
        # queryset类型的数据集
        school_list = School.objects.all()
        # queryset类型数据序列化成
        ss = SchoolSerializer(school_list, many=True)
        return Response(ss.data)

    def post(self, request, *args, **kwargs):
        """
        新增学校接口
        """
        ss = SchoolSerializer(data=request.data, many=False, context={'request': request})
        if ss.is_valid():
            ss.save()
            return Response(ss.data)
        else:
            return HttpResponse(ss.errors)

         
class SchoolDetailView(APIView):
    authentication_classes = [LoginAuth, ]

    def get(self, request, pk, *args, **kwargs):
        """
        查询指定学校列表接口
        """
        try:
            school = School.objects.get(pk=pk)
            ss = SchoolSerializer(school, many=False, context={'request': request})
            return Response(ss.data)
        except School.DoesNotExist as e:
            return HttpResponse('学校不存在')

    def put(self, request, pk, *args, **kwargs):
        """
        修改指定学校信息接口
        """
        try:
            school = School.objects.get(pk=pk)
            ss = SchoolSerializer(school, data=request.data)
            if ss.is_valid():
                ss.save()
                return Response(ss.data)
            else:
                return HttpResponse(ss.errors)
        except School.DoesNotExist as e:
            return HttpResponse('学校不存在')

    def delete(self, request, pk, *args, **kwargs):
        try:
            School.objects.get(pk=pk).delete()
            if School.objects.get(pk=pk):
                return HttpResponse('删除成功')
            else:
                return HttpResponse('删除失败')
        except School.DoesNotExist as e:
            return HttpResponse('学校不存在')
