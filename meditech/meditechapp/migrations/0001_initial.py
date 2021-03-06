# Generated by Django 3.2 on 2021-04-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('radio', models.CharField(blank=True, max_length=200, null=True)),
                ('bloodGrp', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('disease', models.BooleanField(default=False)),
            ],
        ),
    ]
