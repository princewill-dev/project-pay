# Generated by Django 5.0.3 on 2024-05-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0044_alter_payment_converted_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='converted_amount',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
    ]
