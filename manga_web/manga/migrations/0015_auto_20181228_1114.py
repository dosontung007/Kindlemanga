# Generated by Django 2.0.8 on 2018-12-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0014_auto_20181228_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
