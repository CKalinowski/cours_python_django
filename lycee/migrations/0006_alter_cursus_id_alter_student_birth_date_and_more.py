# Generated by Django 4.0.4 on 2022-04-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0005_auto_20220414_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default='2000-01-01', verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
