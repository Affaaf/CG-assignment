from django.contrib import admin
from .models import Post, Application
# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('post_text', 'created_at', 'occupied')


admin.site.register(Post)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('file', 'first_name', 'last_name', 'email_address', 'application_created_at')


admin.site.register(Application, ApplicationAdmin)