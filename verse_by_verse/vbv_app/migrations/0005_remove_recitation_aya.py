# Generated by Django 5.0.4 on 2024-04-22 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vbv_app', '0004_alter_aya_verse_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recitation',
            name='aya',
        ),
    ]