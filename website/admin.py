from django.contrib import admin

from .models import About, CV, Base, Skill, SkillCategory, SkillSession, Education, Project, \
    Experience, Certification, Award, Dossier

admin.site.register(About)
admin.site.register(CV)
admin.site.register(Base)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Award)
admin.site.register(Dossier)
admin.site.register(SkillSession)
