from django.db import models
from category.models import Category

class Reports(models.Model):
    reports_name = models.CharField(max_length=99, null=False, unique=True)
    category = models.ForeignKey(Category,related_name='Category',on_delete=models.CASCADE)
    class Meta:
        db_table = 'apps_reports'

    def __str__(self):
        return self.reports_name
class Industry(models.Model):
    industry_name = models.CharField(max_length=99, unique=True)
    
    class Meta:
        db_table = 'apps_industries'

    def __str__(self):
        return self.industry_name

class Reports_Departments(models.Model):
    departments_name = models.CharField(max_length=99, null=False, unique=True)
    class Meta:
        db_table = 'apps_departments'

    def __str__(self):
        return self.departments_name
class Reports_Month(models.Model):
    month_name = models.CharField(max_length=99, null=False, unique=True)
    quarter = models.CharField(max_length=99, null=False) 

    class Meta:
        db_table = 'apps_month'

    def __str__(self):
        return 'tháng {}'.format(self.month_name)


class Reports_Date(models.Model):
    day = models.CharField(max_length=99, null=False)
    year = models.CharField(max_length=99, null=False)
    month = models.ForeignKey(Reports_Month,on_delete=models.CASCADE,related_name='Reports_Month')
    class Meta:
        db_table = 'apps_date'

    def __str__(self):
        return '{}/{}/{}'.format(self.day, self.month, self.year)
class Reports_Revenue(models.Model):
    tax_amount = models.CharField(max_length=99, null=False)
    total_including_tax = models.CharField(max_length=99, null=False)
    total_excluding_tax = models.CharField(max_length=99, null=False)
    date = models.ForeignKey(Reports_Date,on_delete=models.CASCADE,default='no value',related_name='Revenue_Date')
    departments = models.ForeignKey(Reports_Departments,on_delete=models.CASCADE,default='no value',related_name='Revenue_Departments')
    reports = models.ForeignKey(Reports,on_delete=models.CASCADE,default='no value',related_name='Revenue_Reports')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='Revenue_Industry')
    class Meta:
        db_table = 'apps_reports_revenue'
class Reports_Profit(models.Model):
    profit = models.CharField(max_length=99, null=False)
    net_profit = models.CharField(max_length=99, null=False)
    gross_profit = models.CharField(max_length=99, null=False)
    date = models.ForeignKey(Reports_Date,on_delete=models.CASCADE,default='no value',related_name='Profit_Date')
    departments = models.ForeignKey(Reports_Departments,on_delete=models.CASCADE,default='no value',related_name='Profit_Departments')
    reports = models.ForeignKey(Reports,on_delete=models.CASCADE,default='no value',related_name='Profit_Reports')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='Profit_Industry')
    class Meta:
        db_table = 'apps_reports_profit'