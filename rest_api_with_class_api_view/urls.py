from django.urls import path
from .views import ListEmployeesAPIView, DetailEmployeesAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', ListEmployeesAPIView.as_view()),
    path('api/details/<int:id>', DetailEmployeesAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
