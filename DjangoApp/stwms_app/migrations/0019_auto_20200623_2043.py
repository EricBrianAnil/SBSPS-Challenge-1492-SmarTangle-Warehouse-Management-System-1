# Generated by Django 3.0.3 on 2020-06-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stwms_app', '0018_auto_20200623_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterialbatches',
            name='quality_score',
            field=models.FloatField(),
        ),
    ]
