# Generated by Django 5.0.1 on 2024-04-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
