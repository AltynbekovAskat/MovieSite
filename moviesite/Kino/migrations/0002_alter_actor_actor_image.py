# Generated by Django 5.1.2 on 2024-11-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(blank=True, null=True, upload_to='actor_image'),
        ),
    ]