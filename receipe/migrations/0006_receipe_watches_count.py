# Generated by Django 4.2.3 on 2024-01-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0005_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='watches_count',
            field=models.IntegerField(default=1),
        ),
    ]