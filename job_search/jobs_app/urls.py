from django.urls import path, include
from .views import PostViewset

urlpatterns = [

      path('search-jobs/', PostViewset.as_view()),
]