from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

from website.views import about_view, experience_view, education_view, skill_view, certification_view, \
    certificate_file_view, award_file_view, cv_view, dossier_view, project_view, view_404, view_500

handler404 = view_404
handler500 = view_500
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', about_view, name='about'),
                  path('experience/', experience_view, name='experience'),
                  path('project/', project_view, name='project'),
                  path('education/', education_view, name='education'),
                  path('skill/', skill_view, name='skill'),
                  path('dossier/', dossier_view, name='dossier'),
                  path('certification/', certification_view, name='certification'),
                  path('award/<int:id>', award_file_view, name='award_file'),
                  path('certification/<int:id>', certificate_file_view, name='certificate_file'),
                  path('cv/', cv_view, name='curriculum'),
                  path('404/', view_404),
                  path('500/', view_500),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# change Django admin title
admin.site.site_title = 'My Website Administration'

# change Django admin site header
admin.site.site_header = 'My Website Administration'
