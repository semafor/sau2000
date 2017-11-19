# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ear_tag', models.CharField(max_length=100)),
                ('birth_date_utc', models.DateTimeField(verbose_name='born')),
                ('name', models.CharField(max_length=100)),
                ('main_picture', models.ImageField(upload_to=b'')),
                ('quality', models.CharField(blank=True, choices=[('e', 'E'), ('e-', 'E-'), ('e+', 'E+'), ('u', 'U'), ('u-', 'U-'), ('u+', 'U+'), ('r', 'R'), ('r-', 'R-'), ('r+', 'R+'), ('o', 'O'), ('o-', 'O-'), ('o+', 'O+'), ('p', 'P'), ('p-', 'P-'), ('p+', 'P+')], max_length=2)),
                ('fat_percentage', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('sex', models.CharField(choices=[('m', 'Ram'), ('f', 'Ewe')], max_length=1)),
                ('father', models.ManyToManyField(related_name='_sheep_father_+', to='sau.Sheep')),
                ('mother', models.ManyToManyField(related_name='_sheep_mother_+', to='sau.Sheep')),
            ],
        ),
    ]
