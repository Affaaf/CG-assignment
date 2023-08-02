from django.db import models
from auth_app.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    post_text = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    occupied = models.BooleanField(default=False)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_application_related_name")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_application_related_name")
    file = models.FileField(upload_to='media/', null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField()
    application_created_at = models.DateField(auto_now_add=True, blank=True, null=True)
