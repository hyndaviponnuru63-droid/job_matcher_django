from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import SavedJob

@login_required
def dashboard(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {
        'saved_jobs': saved_jobs
    })

