# Generated by Django 4.2.2 on 2023-06-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bubble_id', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('posX', models.IntegerField()),
                ('posY', models.IntegerField()),
            ],
        ),
    ]
