# Generated by Django 4.2.2 on 2023-06-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0018_alter_dataedge_options_node_node_id_alter_node_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='node_id',
        ),
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
