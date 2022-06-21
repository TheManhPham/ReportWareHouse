from rest_framework.response import Response
from reports.serializers import ReportsSerializer
from .serializers import CategorySerializer
from rest_framework import viewsets,generics,status
from category.models import Category
from rest_framework.decorators import action
from reports.serializers import ReportsSerializer

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(methods=['get'], detail=True, url_path='reports')
    def get_reports(self, request, pk):
        category = Category.objects.get(pk=pk)
        reports = category.Category.all()
        return Response(ReportsSerializer(reports,many=True).data,status=status.HTTP_200_OK)

    
    
        
