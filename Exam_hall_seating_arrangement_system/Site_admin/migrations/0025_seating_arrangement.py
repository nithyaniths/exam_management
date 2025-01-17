# Generated by Django 5.1 on 2024-09-21 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_admin', '0024_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seating_Arrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.PositiveIntegerField()),
                ('examid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.exam')),
                ('hallid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.hall')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site_admin.student')),
            ],
        ),
    ]
