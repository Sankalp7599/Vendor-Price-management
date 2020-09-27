# Generated by Django 2.2.3 on 2019-08-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]
