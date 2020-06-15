from django.shortcuts import render
from wsgiref.util import FileWrapper
from django.http import HttpResponse

import logging

from website.models import About, Experience, Education, Skills, Certification, Dossier, CV, Project

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
    education = Education.objects.all()
    tparms = {
        'educations': education
    }
    logger.info(education)
    return render(request, 'html/pages/education.html', tparms)


def skill_view(request):
    skills = Skills.objects.all()
    tparms = {
        'skills': skills
    }
    logger.info(skills)
    return render(request, 'html/pages/skills.html', tparms)


def certification_view(request):
    certifications = Certification.objects.all()
    tparms = {
        'certifications': certifications
    }
    logger.info(certifications)
    return render(request, 'html/pages/certificates.html', tparms)


def dossier_view(request):
    dossiers = Dossier.objects.all()
    tparms = {
        'dossiers': dossiers
    }
    logger.info(dossiers)
    return render(request, 'html/pages/dossier.html', tparms)


def cv_view(request):
    cv = CV.objects.all().last()
    logger.info('Sending CV')
    wrapper = FileWrapper(cv.curriculum)
    response = HttpResponse(wrapper, content_type='application/pdf')
    return response


def view_404(request, exception):
    return render(request, 'html/status_code/404.html', status=404)
