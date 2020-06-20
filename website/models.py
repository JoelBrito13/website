import base64

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator, EmailValidator
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()
"""
        Base Session
"""
DATE_FORMAT_RETURN = "%B, %Y"


class Base(models.Model):
    title = models.CharField(max_length=50, null=False)
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title


class DateBaseMonthYear(models.Model):
    title = models.CharField(max_length=50, null=False)
    begin_date = models.DateField()
    end_date = models.DateField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title

    @property
    def begin_date_month_year(self):
        return self.begin_date.strftime(DATE_FORMAT_RETURN)

    @property
    def end_date_month_year(self):
        return self.end_date.strftime(DATE_FORMAT_RETURN)


class DateBase(models.Model):
    title = models.CharField(max_length=50, null=False)
    order = models.IntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return f'{self.id} - {self.title}'

    @property
    def date_month_year(self):
        return self.date.strftime(DATE_FORMAT_RETURN)


"""
    Models Session
"""


class About(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=100, validators=[URLValidator])
    github = models.CharField(max_length=150, validators=[URLValidator])
    email = models.CharField(max_length=100, validators=[EmailValidator])


class CV(models.Model):
    curriculum = models.FileField(upload_to='cv', storage=gd_storage)

    @property
    def pdf_drive_share(self):
        return self.curriculum.url.replace("download", "sharing")


class SkillCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.name


class Skill(Base):
    percentage = models.IntegerField(null=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['category', 'order']


class Education(DateBaseMonthYear):
    institution = models.CharField(max_length=50, null=False)
    institution_link = models.CharField(max_length=150, validators=[URLValidator], blank=True, null=True)
    city = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='institution', blank=True, null=True, storage=gd_storage)


class Project(DateBaseMonthYear):
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='projects', blank=True, null=True, storage=gd_storage)
    link = models.CharField(max_length=150, validators=[URLValidator], blank=True, null=True)


class Experience(DateBaseMonthYear):
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='events', blank=True, null=True, storage=gd_storage)


class Certification(DateBase):
    institution = models.CharField(max_length=50, null=False)
    file = models.FileField(upload_to='certificates', storage=gd_storage)

    @property
    def pdf_drive_share(self):
        return self.file.url.replace("download", "sharing")


class Award(DateBase):
    institution = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to='awards', storage=gd_storage)

    @property
    def pdf_drive_share(self):
        return self.file.url.replace("download", "sharing")


class Dossier(DateBase):
    institution = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='dossier', storage=gd_storage)
