# Generated by Django 5.0.6 on 2024-10-01 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0028_exam_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TimeField()),
                ('Duration', models.CharField(max_length=20)),
                ('Semester', models.CharField(max_length=20)),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.exam_date')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.subject')),
            ],
        ),
    ]
