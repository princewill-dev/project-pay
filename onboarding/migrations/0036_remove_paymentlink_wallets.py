# Generated by Django 5.0.3 on 2024-05-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0035_paymentlink_wallets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlink',
            name='wallets',
        ),
    ]
