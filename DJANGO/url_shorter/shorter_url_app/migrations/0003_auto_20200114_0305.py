# Generated by Django 3.0.2 on 2020-01-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter_url_app', '0002_shorter_url_shorty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorter_url',
            name='shorty',
            field=models.CharField(default='', editable=False, max_length=5),
        ),
    ]
