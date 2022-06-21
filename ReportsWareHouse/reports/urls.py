from django.urls import path,include
from rest_framework import routers
from reports.views import ReportsViewSet
router = routers.DefaultRouter()
router.register('reports',ReportsViewSet, 'reports')
urlpatterns = [
    path('',include(router.urls))
]