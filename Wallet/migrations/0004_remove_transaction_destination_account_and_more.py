# Generated by Django 4.0.6 on 2022-08-19 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0003_remove_receipts_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='destination_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='original_account',
        ),
    ]
