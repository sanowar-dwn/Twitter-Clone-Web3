from django.db import models
from django.contrib.auth.models import User
from ..company.models import Company
from ..device.models import Device
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, blank=True, through='DeviceAssignment')

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.get_full_name() or self.user.username