# Generated by Django 2.2.4 on 2019-10-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app22', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savimgsaccountmodel',
            name='photo',
            field=models.ImageField(default=False, upload_to='paramesh/'),
        ),
        migrations.AlterField(
            model_name='savimgsaccountmodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
