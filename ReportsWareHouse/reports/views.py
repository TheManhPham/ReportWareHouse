from .serializers import ParamReportsData, Reports_MonthSerializer
from rest_framework import viewsets,status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db import connection
from .models import Reports_Month
cursor = connection.cursor()
REPORTS_REVENUE = 'apps_reports_revenue'
REPORTS_PROFIT = 'apps_reports_profit'
LEFT_JOIN_DEPARTMENTS = 'LEFT JOIN apps_departments ON apps_reports_revenue.departments_id = apps_departments.id'
LEFT_JOIN_DATE = 'LEFT JOIN apps_date ON apps_reports_revenue.date_id = apps_date.id'
LEFT_JOIN_MONTH = 'LEFT JOIN apps_month ON apps_date.month_id = apps_month.id'
class ReportsViewSet(viewsets.ViewSet):

    @swagger_auto_schema(request_body=ParamReportsData)   
    @action(methods=['post'], detail=True, url_path='get-data')
    def get_data(self,request,pk):
        if not (params := request.data.get('params')):
            return Response("No data",status=status.HTTP_403_FORBIDDEN)
        if (pk == '1'):
            cursor.execute(f'SELECT {params} FROM `{REPORTS_REVENUE}` {LEFT_JOIN_DEPARTMENTS} {LEFT_JOIN_DATE} {LEFT_JOIN_MONTH}')
        if (pk == '2'):
            cursor.execute(f'SELECT {params} FROM {REPORTS_PROFIT} {LEFT_JOIN_DEPARTMENTS} {LEFT_JOIN_DATE} {LEFT_JOIN_MONTH}')
        columns = cursor.description
        result = []
        for value in cursor.fetchall():
            tmp = {columns[index][0]: column for index, column in enumerate(value)}
            result.append(tmp)
        return Response(result,status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='get-fields')
    def get_fields(self,request,pk):
        if (pk == '1'):
            return Response({'tax_amount', 'total_including_tax', 'total_excluding_tax'},status=status.HTTP_200_OK)
        if (pk == '2'):
            return Response({'profit', 'net_profit', 'gross_profit'},status=status.HTTP_200_OK)


# class find_month_by_date_and_year(generics.ListAPIView):
#     serializer_class = Reports_MonthSerializer

#     def get_queryset(self):
#         # print(self.kwargs['date'], '1')
        
#         return Reports_Month.objects.filter(reportsmonth__date = self.kwargs['date'])