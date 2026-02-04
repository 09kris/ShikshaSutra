from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shiksha_sutra.apps.accounts.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('students/', include('shiksha_sutra.apps.students.urls')),
    path('faculty/', include('shiksha_sutra.apps.faculty.urls')),
    path('courses/', include('shiksha_sutra.apps.courses.urls')),
    path('attendance/', include('shiksha_sutra.apps.attendance.urls')),
    path('results/', include('shiksha_sutra.apps.results.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)