# Generated by Django 5.0.6 on 2024-10-02 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0031_alter_seating_arrangement_examid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_ids', models.CharField(max_length=100)),
                ('Shift', models.CharField(max_length=20)),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.exam_date')),
                ('Hallid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hall')),
                ('Invigilator_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.teacher')),
            ],
        ),
    ]