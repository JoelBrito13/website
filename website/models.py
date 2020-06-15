from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator, EmailValidator


class About(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=100, validators=[URLValidator])
    github = models.CharField(max_length=150, validators=[URLValidator])
    email = models.CharField(max_length=100, validators=[EmailValidator])


class CV(models.Model):
    curriculum = models.FileField()


class Base(models.Model):
    title = models.CharField(max_length=50, null=False)
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]
    def __str__(self):
        return self.title


class Skills(Base):
    percentage = models.IntegerField(null=False, validators=[MaxValueValidator(100), MinValueValidator(0)])


class Education(Base):
    institution = models.CharField(max_length=50, null=False)
    institution_link = models.CharField(max_length=150, validators=[URLValidator], blank=True, null=True)
    city = models.CharField(max_length=50, null=False)
    begin_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='institutions/', blank=True, null=True)


class Project(Base):
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    begin_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.CharField(max_length=150, validators=[URLValidator])


class Experience(Base):
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    begin_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)


class Certification(Base):
    institution = models.CharField(max_length=50, null=False)
    date = models.DateField()
    file = models.FileField()


class Award(models.Model):
    institution = models.CharField(max_length=50, null=False)
    date = models.DateField()
    link = models.FileField()


class Dossier(models.Model):
    institution = models.CharField(max_length=50, null=False)
    date = models.DateField()
    image = models.ImageField(upload_to='dossier/')


