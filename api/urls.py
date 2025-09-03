from django.urls import path
from .views import hola
from .views import LoginView

urlpatterns = [
    path('hola/', hola),
    path("login/", LoginView.as_view(), name="login"),
    
]