# Generated by Django 3.2 on 2021-04-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0002_useraccount_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='owner_images'),
        ),
    ]
