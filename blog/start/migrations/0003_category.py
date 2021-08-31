# Generated by Django 3.2.4 on 2021-08-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20210831_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
    ]
