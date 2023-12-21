# Generated by Django 5.0 on 2023-12-21 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_classroom_student_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('roll_no', models.IntegerField()),
                ('bio', models.TextField(max_length=500)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='profile_pictures')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]