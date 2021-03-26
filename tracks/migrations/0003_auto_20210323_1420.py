# Generated by Django 3.1.7 on 2021-03-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20210322_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ManyToManyField(to='tracks.Genre'),
        ),
    ]
