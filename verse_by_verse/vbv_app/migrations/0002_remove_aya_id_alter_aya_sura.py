# Generated by Django 5.0.4 on 2024-04-16 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbv_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aya',
            name='id',
        ),
        migrations.AlterField(
            model_name='aya',
            name='sura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='vbv_app.sura'),
        ),
    ]
