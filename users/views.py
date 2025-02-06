from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
class UserRegistrationView(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    serializer = UserSerializer(data=request.data)

    if request.method == 'GET':
      user = User.objects.all()
      serializer = UserSerializer(user, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
  def post(self, request):
      post_data = JSONParser().parse(request)
      serializer = UserSerializer(data=post_data)
      if serializer.is_valid():
          serializer.save()
          return Response({ "message": "User registered successfully" }, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
    
    # serializer = UserSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({ "message": "User registered successfully" }, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)