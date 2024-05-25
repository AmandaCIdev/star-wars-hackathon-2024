# Generated by Django 5.0.6 on 2024-05-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoda_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
