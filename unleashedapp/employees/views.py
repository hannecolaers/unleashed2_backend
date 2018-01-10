from rest_framework.response import Response

from employees.models import Employee

# Create your views here.
from rest_framework import viewsets, status
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
