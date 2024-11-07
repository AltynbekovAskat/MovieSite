# Generated by Django 5.1.2 on 2024-11-05 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0003_alter_movie_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]