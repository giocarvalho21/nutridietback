# Generated by Django 3.2 on 2021-05-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20210502_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.BooleanField(choices=[('ENABLED', 1), ('DISABLED', 0)]),
        ),
    ]
