# Generated by Django 4.2.2 on 2023-06-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0013_alter_node_options_remove_node_bubble_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]