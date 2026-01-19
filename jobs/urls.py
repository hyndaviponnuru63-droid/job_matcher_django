from django.urls import path
from .views import job_list, save_job
from . import api_views
from .views import save_job, saved_jobs, remove_saved_job, upload_resume

urlpatterns = [
    path('', job_list, name='job_list'),
    path('save/<int:job_id>/', save_job, name='save_job'),

    # API routes
    path('api/jobs/', api_views.job_list_api),
    path('api/jobs/search/', api_views.job_search_api),
    path('api/jobs/save/<int:job_id>/', api_views.save_job_api),
    path('api/saved/', api_views.saved_jobs_api),

    path('save/<int:job_id>/', save_job, name='save_job'),
    path('saved/', saved_jobs, name='saved_jobs'),
    path('remove/<int:job_id>/', remove_saved_job, name='remove_job'),
    path('upload-resume/', upload_resume, name='upload_resume'),
]
