# # models.py
# from django.contrib.auth.models import User
# from django.db import models
# from django.conf import settings


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Priority(models.Model):
#     name = models.CharField(max_length=50)
#     level = models.IntegerField(help_text="Lower number = higher priority")

#     def __str__(self):
#         return f"{self.name} ({self.level})"


# class TaskStatus(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True, null=True)
#     due_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(
#         Category, on_delete=models.SET_NULL, null=True, blank=True)
#     priority = models.ForeignKey(
#         Priority, on_delete=models.SET_NULL, null=True, blank=True)
#     status = models.ForeignKey(
#         TaskStatus, on_delete=models.SET_NULL, null=True, blank=True)
#     assigned_users = models.ManyToManyField(
#         User, related_name='assigned_tasks')
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL,
#                               on_delete=models.CASCADE, null=True)  # Allow nulls
#     file = models.FileField(upload_to='attachments/', blank=True, null=True)

#     def __str__(self):
#         return self.title


# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     def __str__(self):
#         return self.name


# class Settings(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
#     theme = models.CharField(max_length=50, default='light')
#     notifications_enabled = models.BooleanField(default=True)

#     def __str__(self):
#         return self.user.username


# class Attachment(models.Model):
#     file = models.FileField(upload_to='attachments/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.file)


from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(help_text="Lower number = higher priority")

    def __str__(self):
        return f"{self.name} ({self.level})"


class TaskStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(
        TaskStatus, on_delete=models.SET_NULL, null=True, blank=True)

    assigned_users = models.ManyToManyField(
        User, related_name='assigned_tasks')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    file = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # Added OneToOne relation to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.name


class Settings(models.Model):
    # Removed default=1 to make it required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50, default='light')
    notifications_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)
