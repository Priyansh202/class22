from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Class
from .serializers import ClassSerializer

class ClassDetailView(generics.RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
def class_detail(request, pk):
    class_obj = Class.objects.get(pk=pk)
    return render(request, 'template.html', {'class': class_obj})