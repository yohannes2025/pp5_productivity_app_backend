# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Task, Profile, Settings
# from .serializers import TaskSerializer, ProfileSerializer, SettingsSerializer
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.views import APIView


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(assigned_users=self.request.user)

#     def get_queryset(self):
#         return self.queryset.filter(assigned_users=self.request.user)


# class ProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()
#     permission_classes = [IsAuthenticated]


# class SettingsViewSet(viewsets.ModelViewSet):
#     serializer_class = SettingsSerializer
#     queryset = Settings.objects.all()
#     permission_classes = [IsAuthenticated]


# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets, permissions
from .models import Category, Priority, TaskStatus, Task, UserProfile, Settings
from .serializers import CategorySerializer, PrioritySerializer, TaskStatusSerializer, TaskSerializer, ProfileSerializer, UserSerializer, SettingsSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# from django.http import HttpResponse


# def home_view(request):
#     return HttpResponse("Welcome to the API! Please check the /api/ endpoint.")


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
