# Generated by Django 3.2.1 on 2021-05-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=200)),
                ('guid', models.CharField(max_length=200)),
                ('isActive', models.CharField(max_length=200)),
                ('balance', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('eyeColor', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('contactDetails', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('registered', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('friends', models.CharField(max_length=200)),
                ('greetings', models.CharField(max_length=200)),
                ('favoriteFruit', models.CharField(max_length=200)),
            ],
        ),
    ]
