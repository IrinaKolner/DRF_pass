from django.urls import path
from .views import Pereval_addedAPICreate, PerevalOne


urlpatterns = [
    path('submitData/', Pereval_addedAPICreate.as_view()),
    path('submitData/<int:pk>/', PerevalOne.as_view()),
]