
from rest_framework.views import APIView
from .serializers import SignupSerializer, SigninSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse


class SignupViewset(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewset(APIView):

    def post(self, request):
        # serializer = SigninSerializer(data=request.data)
        # if serializer.is_valid():
        #     email = serializer.validated_data["email"]
        #     password = serializer.validated_data["password"]
        email = request.data.get("email")

        password = request.data.get("password")
        print("email",email)
        print("password", password)
        # user = User.objects.filter(email=email, password=password).first()
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response(
                {"status": True,  'refresh': str(refresh), 'access': str(refresh.access_token)},
                status=status.HTTP_200_OK
            )

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # return Response({'error': 'Invalid credentials', 'msg': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
