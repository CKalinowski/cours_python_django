# Generated by Django 4.0.4 on 2022-05-20 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0007_auto_20220415_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursus',
            options={},
        ),
        migrations.AlterField(
            model_name='cursus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='x@y.z', max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default='0999999999', help_text='phone number of the student', max_length=10, verbose_name='Phone number'),
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of call')),
                ('isMissing', models.BooleanField(default=True, verbose_name='Is Missing')),
                ('reason', models.CharField(default='', help_text="Raison de l'absence", max_length=255, verbose_name='Reason')),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.cursus')),
                ('student', models.ManyToManyField(to='lycee.student')),
            ],
        ),
        migrations.CreateModel(
            name='ParticularPresence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of call')),
                ('isMissing', models.BooleanField(verbose_name='Is Missing')),
                ('reason', models.CharField(default='', help_text="Raison de l'absence", max_length=255, verbose_name='Reason')),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.cursus')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.student')),
            ],
        ),
    ]
