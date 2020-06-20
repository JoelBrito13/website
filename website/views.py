from django.shortcuts import render
from wsgiref.util import FileWrapper
from django.http import HttpResponse
import logging

from website.models import About, Experience, Education, Skill, Certification, Dossier, CV, Project, Award, \
    SkillCategory

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'info.log'
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        },
        'debug': {
            'level': 'DEBUG',
            'handlers': ['console', 'debug']
        }
    }
})
logger = logging.getLogger(__name__)

logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)


def about_view(request):
    about = About.objects.all().last()

    tparms = {
        'about': about
    }
    logger.info(about)
    return render(request, 'html/pages/about.html', tparms)


def experience_view(request):
    experiences = Experience.objects.all()
    tparms = {
        'experiences': experiences
    }
    logger.info(experiences)
    return render(request, 'html/pages/experience.html', tparms)


def project_view(request):
    projects = Project.objects.all()
    tparms = {
        'projects': projects
    }
    logger.info(projects)
    return render(request, 'html/pages/project.html', tparms)


def education_view(request):
    educations = Education.objects.all()
    tparms = {
        'educations': educations
    }
    logger.info(educations)
    return render(request, 'html/pages/education.html', tparms)


def skill_view(request):
    skills = Skill.objects.all()
    skill_categories = SkillCategory.objects.all()
    categories = {}
    for category in skill_categories:
        categories[category.name] = []
    for item in skills:
        categories[item.category.name].append(item)
    tparms = {

        'categories': categories
    }
    logger.info(categories)
    return render(request, 'html/pages/skills.html', tparms)


def certification_view(request):
    certifications = Certification.objects.all()
    awards = Award.objects.all()
    tparms = {
        'certifications': certifications,
        'awards': awards
    }
    logger.info(tparms)
    return render(request, 'html/pages/certificates.html', tparms)


def dossier_view(request):
    dossiers = Dossier.objects.all()
    tparms = {
        'dossiers': dossiers
    }
    logger.info(dossiers)
    return render(request, 'html/pages/dossier.html', tparms)


def award_file_view(request, id):
    award = Award.objects.get(id=id)
    logger.info(award)
    if award.file:
        try:
            tparms = {
                'title': 'Curriculum',
                'file': award
            }
            return render(request, 'html/pages/pdf_display.html', tparms)
        except TypeError:
            pass
    tparms = {
        'title': 'Award',
        'message': 'Award not found'
    }
    return render(request, 'html/pages/no-content.html', tparms)


def certificate_file_view(request, id):
    certificate = Certification.objects.get(id=id)
    logger.info(certificate)
    if certificate.file:
        try:
            tparms = {
                'title': 'Certificate',
                'file': certificate
            }
            return render(request, 'html/pages/pdf_display.html', tparms)
        except TypeError:
            pass
    tparms = {
        'title': 'Certification',
        'message': 'Certification not found'
    }
    return render(request, 'html/pages/no-content.html', tparms)


def cv_view(request):
    cv = CV.objects.all().last()
    logger.info('Sending CV')
    if cv and cv.curriculum:
        try:
            tparms = {
                'title': 'Curriculum',
                'file': cv
            }
            return render(request, 'html/pages/pdf_display.html', tparms)
        except TypeError:
            pass
    tparms = {
        'title': 'Curriculum',
        'message': 'Curriculum not found'
    }
    return render(request, 'html/pages/no-content.html', tparms)


def view_404(request, exception):
    return render(request, 'html/status_code/404.html', status=404)


def view_500(request):
    return render(request, 'html/status_code/500.html', status=500)
