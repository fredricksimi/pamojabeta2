# Generated by Django 4.0.4 on 2022-06-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
