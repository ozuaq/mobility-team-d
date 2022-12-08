# Generated by Django 4.1.4 on 2022-12-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_app', '0002_alter_testmedia_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='a_app.testtag')),
            ],
        ),
    ]
