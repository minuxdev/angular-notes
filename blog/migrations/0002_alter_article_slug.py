# Generated by Django 5.0 on 2023-12-24 01:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, default=None, editable=False, null=True, populate_from='topic', unique_with=['author']),
        ),
    ]
