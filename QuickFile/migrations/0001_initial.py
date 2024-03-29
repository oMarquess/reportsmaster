# Generated by Django 3.2.8 on 2021-10-23 05:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('report_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('wbc', models.FloatField()),
                ('hb', models.FloatField()),
                ('rbc', models.FloatField()),
                ('plt', models.FloatField()),
                ('lym', models.FloatField()),
                ('lym_p', models.FloatField()),
                ('hct', models.FloatField()),
                ('pcv', models.FloatField()),
                ('mch', models.FloatField()),
                ('mchc', models.FloatField()),
                ('mcv', models.FloatField()),
                ('rdw', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'CBC',
            },
        ),
    ]
