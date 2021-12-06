from django.http import JsonResponse, HttpResponse
from rest_framework import views, status, parsers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import CourseSerializer
from .models import Course


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def courses_list(request):
    """
        List all courses or create a new course
        RPS - requests per second
    """
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(instance=courses, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def courses_detail(request, pk):
    """
        Retrieve, update or delete a course
        courses/1/
    """
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(instance=course)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method in {"PUT", "PATCH"}:
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(instance=course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    elif request.method == "DELETE":
        course.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
