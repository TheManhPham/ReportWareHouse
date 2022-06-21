from django.contrib import admin
from category.models import Category
from reports.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Reports)
admin.site.register(Reports_Month)
admin.site.register(Reports_Profit)
admin.site.register(Reports_Revenue)
admin.site.register(Reports_Date)
admin.site.register(Reports_Departments)
