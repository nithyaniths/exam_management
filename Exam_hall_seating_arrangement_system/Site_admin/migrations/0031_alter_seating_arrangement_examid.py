# Generated by Django 5.0.6 on 2024-10-02 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0030_seating_arrangement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seating_arrangement',
            name='examid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.exam_date'),
        ),
    ]