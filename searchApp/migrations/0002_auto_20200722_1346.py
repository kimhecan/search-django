# Generated by Django 3.0.6 on 2020-07-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=10),
        ),
    ]