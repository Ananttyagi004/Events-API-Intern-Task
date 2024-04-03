from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class EventList(APIView):
    def get(self,request,format=None):
        events=Event.objects.all()
        serializer=EventSerializer(events,many=True)
        return  Response(serializer.data,status=status.HTTP_200_OK)
    
class EventAdd(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Event Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk,format=None):
        events=Event.objects.get(id=pk)
        serializer=EventSerializer(events)
        return  Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        event=Event.objects.get(id=pk)
        serializer=EventSerializer(event,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_200_OK)
        return  Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk,format=None):
        events=Event.objects.get(id=pk)
        serializer=EventSerializer(events,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_200_OK)
        return  Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)  
    
    def delete(self,request,pk,format=None):
        events=Event.objects.get(id=pk)
        if Event is not None:
            events.delete()
            return Response({'msg':'Event Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'msg':'Something went wrong'},status=status.HTTP_404_NOT_FOUND)

