# Generated by Django 4.2.7 on 2024-06-25 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0064_paymentlink_callback_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlink',
            name='callback_url',
        ),
    ]
