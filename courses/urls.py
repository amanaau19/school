from django.urls import path
from .views import courses_list, courses_detail


urlpatterns = [
    path("courses/", courses_list, name="course-list"),
    path("courses/<int:pk>/", courses_detail, name="course-detail"),
]
