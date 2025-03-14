# Generated by Django 5.1.6 on 2025-02-14 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='queixar',
        ),
        migrations.AddField(
            model_name='pacientes',
            name='queixa',
            field=models.CharField(choices=[('TDAH', 'TDAH'), ('D', 'Depressão'), ('A', 'Ansiedade'), ('TAG', 'Transtorno de ansiedade generalizada')], default='TDAH', max_length=4),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
