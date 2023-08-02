from django.urls import path, include
from .views import SignupViewset, LoginViewset

urlpatterns = [

      path('signup/', SignupViewset.as_view()),
      path("login/", LoginViewset.as_view()),


]