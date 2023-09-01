from django.urls import path
from .views import DeviceList, DeviceDetail, DeviceAssignmentDetail, DeviceAssignmentList

urlpatterns = [
    path('devices/', DeviceList.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceDetail.as_view(), name='device-detail'),

    path('device-assignments/', DeviceAssignmentList.as_view(), name='device-assignment-list'),
    path('device-assignments/<int:pk>/', DeviceAssignmentDetail.as_view(), name='device-assignment-detail'),   
]
