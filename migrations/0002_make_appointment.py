# Generated by Django 5.0.1 on 2024-03-14 11:10

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('myadmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Make_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('time', models.CharField(max_length=30)),
                ('remarks', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('reason', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer_register')),
                ('physio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('physio_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.physio_clinic')),
            ],
            options={
                'db_table': 'make_appointment',
            },
        ),
    ]
