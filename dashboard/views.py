from django.contrib.auth.decorators import login_required
from jobs.models import SavedJob, Job
from django.db.models import Count
from django.shortcuts import render


@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {
        'saved_jobs': SavedJob.objects.filter(user=request.user).count(),
        'jobs_by_location': Job.objects.values('location').annotate(total=Count('id'))
    })

@login_required
def dashboard(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {
        'saved_jobs': saved_jobs
    })

