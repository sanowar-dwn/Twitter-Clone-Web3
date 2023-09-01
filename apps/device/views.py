from rest_framework import generics
from .models import Device
from .serializers import DeviceSerializer
from .models import DeviceAssignment
from .serializers import DeviceAssignmentSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceAssignmentList(generics.ListCreateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
    

class DeviceAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
