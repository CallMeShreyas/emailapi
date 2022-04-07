# from employeeapi.viewsets import EmployeeViewset
from simple.viewsets import EmailViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register("emaildb",EmailViewset)

