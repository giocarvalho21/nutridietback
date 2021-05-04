# Generated by Django 3.2 on 2021-05-02 13:35

from django.db import migrations, models
import person.enum.enum_generic_status
import person.enum.enum_generic_type


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20210502_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='personphone',
            name='status',
            field=models.IntegerField(choices=[('ENABLED', 1), ('DISABLED', 0)], default=1),
        ),
        migrations.AddField(
            model_name='personphone',
            name='type',
            field=models.IntegerField(choices=[('MAIN', 1), ('WORK', 2), ('COMMERCIAL', 3), ('ADDITIONAL', 4)], default=1),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
