# Generated by Django 5.0.3 on 2024-05-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0047_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token_logo',
            field=models.FileField(blank=True, null=True, upload_to='token_logos'),
        ),
    ]
