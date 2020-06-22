from rest_app01.serializer.serializer import SchoolSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_app01.models.school import School
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


class SchoolListView(APIView):
    def get(self, request, *args, **kwargs):
        """
        查询学校列表接口
        """
        school_list = School.objects.all()
        ss = SchoolSerializer(school_list, many=True)
        # return HttpResponse('get')
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