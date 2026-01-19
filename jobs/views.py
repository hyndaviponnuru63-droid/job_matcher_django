from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, SavedJob, Resume
import PyPDF2
from .utils import extract_skills


def job_list(request):
    jobs = Job.objects.all()

    keyword = request.GET.get('q')
    location = request.GET.get('location')
    skill = request.GET.get('skill')
    if keyword:
        jobs = jobs.filter(
            Q(title__icontains=keyword) |
            Q(company__icontains=keyword) |
            Q(description__icontains=keyword)
        )
    if location:
        jobs = jobs.filter(location__icontains=location)
    if skill:
        jobs = jobs.filter(skills__icontains=skill)
    resume = Resume.objects.filter(user=request.user).first()

    for job in jobs:
        job.match = match_score(
            job.skills_required,
            resume.extracted_skills if resume else ""
        )
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs
    })


@login_required
def save_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    SavedJob.objects.get_or_create(
        user=request.user,
        job=job
    )
    return redirect('job_list')
