from rest_framework.decorators import api_view
from .models import Booking_table, Menu_table
from .serializers import UserSerializer,BookingSerialize,MenuSerialize
from rest_framework import generics
from django.shortcuts import render


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Booking_table.objects.all()
    serializer_class = BookingSerialize
    

class SingleMenuItemView( generics.ListCreateAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = MenuSerialize
