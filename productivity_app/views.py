
# productivity_app/views.py
from rest_framework import viewsets, permissions
from .models import Category, Priority, TaskStatus, Task, UserProfile, Settings
from .serializers import CategorySerializer, PrioritySerializer, TaskStatusSerializer, TaskSerializer, ProfileSerializer, UserSerializer, SettingsSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class SettingsViewSet(viewsets.ModelViewSet):
    # Adjust the queryset based on your requirements
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer  #
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Optionally assign the owner or any other logic during the creation of settings
        # Uncomment if your Settings model has an 'owner' field
        serializer.save(owner=self.request.user)
