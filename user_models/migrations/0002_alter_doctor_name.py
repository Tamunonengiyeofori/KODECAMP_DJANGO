# Generated by Django 4.0.5 on 2022-06-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
