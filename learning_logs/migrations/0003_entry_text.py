# Generated by Django 4.2.16 on 2024-09-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
