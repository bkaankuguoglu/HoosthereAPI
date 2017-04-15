from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Visitor
from .serializer import VisitorSerializer
from rest_framework import mixins
from rest_framework import generics


# Lists all visitors or creates a new one
# /visitors


# Class-based API Views using generics

class VisitorList(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

# Class-based API Views using mixins

""""
class VisitorList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VisitorDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""

# Class-based API Views

""""
class VisitorList(APIView):

    def get(self, request):
        visitors = Visitor.objects.all()
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitorDetail(APIView):

    def get(self, request, visitor_id):
        visitor = get_object_or_404(Visitor, pk=visitor_id)
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    def put(self, request, visitor_id):
        visitor = get_object_or_404(Visitor, pk=visitor_id)
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, visitor_id):
        visitor = get_object_or_404(Visitor, pk=visitor_id)
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
"""