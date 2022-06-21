from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=99, null=False, unique=True)

    class Meta:
        db_table = 'apps_category'

    def __str__(self):
        return self.name
    
