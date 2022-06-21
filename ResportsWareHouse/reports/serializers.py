from rest_framework import serializers
from reports.models import Reports,Reports_Revenue, Reports_Date, Reports_Month, Reports_Departments, Reports_Profit
# PARAM
class ParamReportsData(serializers.Serializer):
    params = serializers.CharField( required= False)
# SERIALIZER
class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'
class Reports_MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports_Month
        fields = ['name','quarter']
class Reports_DateSerializer(serializers.ModelSerializer):
    month = Reports_MonthSerializer()
    class Meta:
        model = Reports_Date
        fields = ['day','year','month']
class Reports_Departments(serializers.ModelSerializer):
    class Meta:
        model = Reports_Departments
        fields = ['name']
class Reports_RevenueSerializer(serializers.ModelSerializer):
    departments = Reports_Departments()
    date = Reports_DateSerializer()
    # reports = ReportsSerializer()
    class Meta:
        model = Reports_Revenue
        fields = ['tax_amount','total_including_tax','total_excluding_tax','date','departments']
class Reports_ProfitSerializer(serializers.ModelSerializer):
    departments = Reports_Departments()
    date = Reports_DateSerializer()
    # reports = ReportsSerializer()
    class Meta:
        model = Reports_Profit
        fields = ['id','profit','net_profit','gross_profit','date','departments']