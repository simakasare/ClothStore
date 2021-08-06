from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import RegistrationSerializer

@api_view(['POST,'])
def registration_view(request):
    if request.method =='POST':
        Serializer = RegistrationSerializer(data=request.data)
        data={}
        if Serializer.is_valid():
            account=Serializer.save()
            data['response']="successfully register new user"
            data['email']=account.email
            data['username']=account.username

        else:
            data=Serializer.errors
        return Response(data)
            



# Create your views here.
