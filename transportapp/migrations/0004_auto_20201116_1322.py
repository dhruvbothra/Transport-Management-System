# Generated by Django 3.1.3 on 2020-11-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0003_auto_20201115_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripprofile',
            name='destination2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='destination3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='destination4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='destination5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='good_type2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='good_type3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='good_type4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tripprofile',
            name='good_type5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
