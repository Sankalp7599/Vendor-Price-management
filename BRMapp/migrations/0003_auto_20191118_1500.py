# Generated by Django 2.2.3 on 2019-11-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRMapp', '0002_brmuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('distributer', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
