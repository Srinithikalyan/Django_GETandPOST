from django.conf.urls import url, include

from rest_framework import routers

from .views import DisplayView, EmployeeView

router = routers.DefaultRouter()
router.register('get employee details', DisplayView, base_name='employee_details')
router.register('employee details', EmployeeView, base_name='employee_details')


urlpatterns = [
    url(r'^', include(router.urls)),
]
