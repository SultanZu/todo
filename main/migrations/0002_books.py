# Generated by Django 3.1.3 on 2021-01-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subtitle', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=5)),
                ('genre', models.CharField(max_length=15)),
                ('author', models.CharField(max_length=15)),
                ('year', models.CharField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
