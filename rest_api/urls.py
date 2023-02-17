from django.urls import path
from .views import list_post, posts_details

urlpatterns = [
    path('api/', list_post),
    path('details/<int:id>', posts_details)
]
