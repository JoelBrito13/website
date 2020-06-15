from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static

from website.views import about_view, experience_view, education_view, skill_view, certification_view, cv_view, \
    dossier_view, project_view#, view_404

handler404 = 'website.views.view_404'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', about_view, name='about'),
                  path('experience/', experience_view, name='experience'),
                  path('project/', project_view, name='project'),
                  path('education/', education_view, name='education'),
                  path('skill/', skill_view, name='skill'),
                  path('dossier/', dossier_view, name='dossier'),
                  path('certification/', certification_view, name='certification'),
                  path('cv/', cv_view, name='curriculum'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
