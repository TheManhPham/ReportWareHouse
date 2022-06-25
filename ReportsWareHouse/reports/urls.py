from django.urls import path,include
from rest_framework import routers
from reports.views import ReportsViewSet, find_month_by_date_and_year
router = routers.DefaultRouter()
router.register('reports',ReportsViewSet, 'reports')
urlpatterns = [
    path('',include(router.urls)),
    # path('find/<int:date>/<int:yearStart>/<int:yearEnd>/',find_month_by_date_and_year.as_view(),name='date')
]