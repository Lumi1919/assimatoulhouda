# Generated by Django 3.2.2 on 2021-05-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arif',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='membres/static'),
        ),
    ]