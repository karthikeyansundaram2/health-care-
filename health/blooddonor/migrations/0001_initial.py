# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-20 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloodbankregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BLoodBankName', models.CharField(max_length=45)),
                ('BloodBankAddress', models.CharField(max_length=300)),
                ('BloodBankMobileNumber', models.CharField(max_length=10)),
                ('BloodBankEmailId', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BloodGroup', models.CharField(max_length=5)),
                ('TypeOfBlood', models.CharField(max_length=3)),
                ('Date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Time', models.TimeField(blank=True, null=True)),
                ('NearByBloodBank', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='donorregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DonorName', models.CharField(max_length=50)),
                ('DonorAddress', models.CharField(max_length=300)),
                ('DonorMobileNumber', models.CharField(max_length=10)),
                ('DonorAge', models.CharField(max_length=3)),
                ('DonorEmailId', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BloodGroup', models.CharField(max_length=5)),
                ('TypeOfBlood', models.CharField(max_length=3)),
                ('NumberOfUnits', models.IntegerField()),
                ('Date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hospitalregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HospitalName', models.CharField(max_length=50)),
                ('HospitalAddress', models.CharField(max_length=300)),
                ('HospitalMobileNumber', models.CharField(max_length=10)),
                ('HospitalEmailId', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LoginName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('User', models.CharField(choices=[('bloodbank', 'BLOODBANK'), ('hospital', 'HOSPITAL'), ('donor', 'DONOR')], default='bloodbank', max_length=20)),
            ],
        ),
    ]