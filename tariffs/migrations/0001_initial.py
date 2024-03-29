# Generated by Django 4.2.6 on 2023-11-06 09:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("meters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tariff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("metric_prefix", models.SmallIntegerField()),
                ("price", models.FloatField()),
                ("start_date", models.DateField(default=datetime.datetime.today)),
                (
                    "meter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="meters.meter"
                    ),
                ),
            ],
        ),
    ]
