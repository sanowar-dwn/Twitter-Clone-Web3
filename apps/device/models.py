from django.db import models
from ..company.models import Company
from ..employee.models import Employee
# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=255, default='Good')
    checked_out = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'DeviceAssignment'
        verbose_name_plural = 'DeviceAssignment'
        ordering = ['-updated_at']  # from top to bottom
        db_table = 'DeviceAssignment'

    def __str__(self):
        if self.return_date:
            return f"{self.device.name} returned by {self.employee.user.get_username()} at: ({self.return_date.ctime()})"
        return f"{self.device.name} assigned to {self.employee.user.get_username()}, at: ({self.assigned_date.ctime()})"
