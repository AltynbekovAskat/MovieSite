# Generated by Django 5.1.2 on 2024-11-10 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0006_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kino.movie'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]