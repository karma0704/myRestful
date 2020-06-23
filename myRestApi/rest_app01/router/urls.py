from django.urls import path
from rest_app01.views import school
from rest_app01.views import school_v1
from rest_app01.views import school_v2
from rest_app01.views import school_v3



urlpatterns = [
    # rest接口v1.0.0版本url设置
    path('schools', school.SchoolListView.as_view(), name='schools'),
    path('schools/<int:pk>', school.SchoolDetailView.as_view(), name='schoolDetail'),
    # rest接口v1.1.0版本url设置
    path('v1/schools', school_v1.SchoolListView.as_view(), name='schools_v1'),
    path('v1/schools/<int:pk>', school_v2.SchoolDetailView.as_view(), name='schoolDetail_v1'),
    # rest接口v1.2.0版本url设置
    path('v2/schools', school_v1.SchoolListView.as_view(), name='schools_v2'),
    path('v2/schools/<int:pk>', school_v2.SchoolDetailView.as_view(), name='schoolDetail_v2'),
    # rest接口v2.0.0版本url设置
    path('v3/schools', school_v3.SchoolViewSet.as_view({
            'get': 'list', 
            'post': 'create'
        }), name='school_v3'),
    path('v3/schools/<int:pk>', school_v3.SchoolViewSet.as_view({
            'get': 'retrieve', 
            'put': 'update', 
            'delete': 'destroy'
        }), name='schoolDetail_v3'),
]