# Generated by Django 3.0.4 on 2020-06-20 19:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=100, validators=[django.core.validators.URLValidator])),
                ('github', models.CharField(max_length=150, validators=[django.core.validators.URLValidator])),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator])),
            ],
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='cv')),
            ],
        ),
        migrations.CreateModel(
            name='DateBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='DateBaseMonthYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('datebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBase')),
                ('institution', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='awards')),
            ],
            bases=('website.datebase',),
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('datebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBase')),
                ('institution', models.CharField(max_length=50)),
                ('file', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='certificates')),
            ],
            bases=('website.datebase',),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('datebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBase')),
                ('institution', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='dossier')),
            ],
            bases=('website.datebase',),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('datebasemonthyear_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBaseMonthYear')),
                ('institution', models.CharField(max_length=50)),
                ('institution_link', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.URLValidator])),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='institution')),
            ],
            bases=('website.datebasemonthyear',),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('datebasemonthyear_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBaseMonthYear')),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='events')),
            ],
            bases=('website.datebasemonthyear',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('datebasemonthyear_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.DateBaseMonthYear')),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='projects')),
                ('link', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.URLValidator])),
            ],
            bases=('website.datebasemonthyear',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.Base')),
                ('percentage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.SkillCategory')),
            ],
            options={
                'ordering': ['category', 'order'],
            },
            bases=('website.base',),
        ),
    ]