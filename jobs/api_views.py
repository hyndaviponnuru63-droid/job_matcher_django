from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from .models import Job, SavedJob
from .serializers import JobSerializer, SavedJobSerializer


# -----------------------------
# JOB LIST API (WITH PAGINATION)
# -----------------------------
@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 5   # jobs per page

    result_page = paginator.paginate_queryset(jobs, request)
    serializer = JobSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


# ---------------------------------
# JOB SEARCH + FILTER API (STEP 13C)
# ---------------------------------
@api_view(['GET'])
def job_search_api(request):
    q = request.GET.get('q')
    location = request.GET.get('location')
    skill = request.GET.get('skill')

    jobs = Job.objects.all()

    if q:
        jobs = jobs.filter(
            Q(title__icontains=q) |
            Q(company__icontains=q) |
            Q(description__icontains=q)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    if skill:
        jobs = jobs.filter(skills__icontains=skill)

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


# -----------------------------
# SAVE JOB API (AUTH REQUIRED)
# -----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_job_api(request, job_id):
    job = Job.objects.get(id=job_id)
    SavedJob.objects.get_or_create(user=request.user, job=job)

    return Response({
        "status": "success",
        "message": "Job saved successfully"
    })


# -----------------------------
# SAVED JOBS LIST API
# -----------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saved_jobs_api(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)
    serializer = SavedJobSerializer(saved_jobs, many=True)
    return Response(serializer.data)
