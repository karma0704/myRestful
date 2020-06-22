from django.urls import path
from rest_app01.views.school import SchoolListView, SchoolDetailView



urlpatterns = [
    path('schools/', SchoolListView.as_view(), name='schools'),
    path('schools/<int:pk>', SchoolDetailView.as_view(), name='schoolDetail'),
]