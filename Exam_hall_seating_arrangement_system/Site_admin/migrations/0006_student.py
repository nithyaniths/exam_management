# Generated by Django 5.0.6 on 2024-09-16 05:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0005_teacher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=20)),
                ('Semester', models.CharField(max_length=20)),
                ('Mobile', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]