from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import ResourceCentreSerializer
from .serializers import NewsCentreSerializer
from .serializers import JournalistSerializer
from .models import Journalist
from .models import ResourceCentre
from .models import NewsCentre
from uuid import uuid4


# Create your views here.

class ResourceCentreViewSet(viewsets.ViewSet):

    def create(self, request, format=None):
        data = request.data
        try:
             resource, created = ResourceCentre.objects.get_or_create(id=uuid4(), journalist_fname=data['journalist_fname'],
                                                 journalist_lname=data['journalist_lname'],
                                                 current_status=data['current_status'],
                                                 assigned_date=data['assigned_date'],
                                                 journalist_id=data['journalist_id'],
                                                 newscentre_id=data['newscentre_id'])
        except Exception as e:
             return Response(status=status.HTTP_409_CONFLICT,data={"Message":"This article is already assigned."})
        return Response(status=status.HTTP_201_CREATED,data={"Message":"Article is assigned."})

    def list(self, request):
        queryset = ResourceCentre.objects.all()
        serializer = ResourceCentreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ResourceCentre.objects.filter(journalist_fname=request.GET.get("first_name"),
                                                 journalist_lname=request.GET.get("last_name"))
        resource = get_object_or_404(queryset)
        serializer = ResourceCentreSerializer(resource)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            ResourceCentre.objects.filter(id=pk).delete()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data={"Message":"This article is not assigned."})
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalistViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Journalist.objects.all()
        serializer = JournalistSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journalist.objects.filter(first_name=request.GET.get("first_name"),
                                             last_name=request.GET.get("last_name"))
        journalist = get_object_or_404(queryset)
        serializer = JournalistSerializer(journalist)
        return Response(serializer.data)


class NewsCentreViewSet(viewsets.ModelViewSet):
    queryset = NewsCentre.objects.all()
    serializer_class = NewsCentreSerializer
