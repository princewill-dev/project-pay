# Generated by Django 5.0.3 on 2024-05-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0050_rename_store_description_paymentlink_link_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
