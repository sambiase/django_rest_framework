from django.urls import path
from .views import students_list_post, posts_details

urlpatterns = [
    path('api/', students_list_post),
    path('details/<int:id>', posts_details)
]
