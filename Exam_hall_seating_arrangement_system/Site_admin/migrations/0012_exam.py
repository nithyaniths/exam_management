# Generated by Django 5.0.6 on 2024-09-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0011_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Duration', models.CharField(max_length=20)),
                ('Semester', models.CharField(max_length=20)),
            ],
        ),
    ]
