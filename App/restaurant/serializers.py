from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking_table,Menu_table
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
class BookingSerialize(serializers.ModelSerializer):
    class Meta:
        model=Booking_table
        fields='__all__'

class MenuSerialize(serializers.ModelSerializer):
    class Meta:
        model=Menu_table
        fields='__all__'