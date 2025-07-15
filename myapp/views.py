from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student
from rest_framework import generics, permissions
def home(request):
    return HttpResponse("Welcome to the Student Management App!")

# Student API (Protected with JWT)
class StudentListAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Enforce JWT protection
# Registration API with JWT generation
class RegisterAPI(generics.CreateAPIView):
    permission_classes = [AllowAny]  # Public endpoint
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

# Login API with JWT generation
class LoginView(APIView):
    permission_classes = [AllowAny]  # Public endpoint

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response({
                "success": True,
                "status_code": 200,
                "message": "User Logged in",
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
class ApiRoot(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Welcome to your Student Management API",
            "endpoints": {
                "students": "/api/students/",
                "register": "/api/register/",
                "login": "/api/login/",
            }
        })