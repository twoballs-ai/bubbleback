# Generated by Django 4.2.2 on 2023-06-30 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0014_alter_node_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datanode',
            options={'verbose_name': 'Данные для Ноды', 'verbose_name_plural': 'Данные для Ноды'},
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': 'Ноды', 'verbose_name_plural': 'Ноды'},
        ),
        migrations.AlterModelOptions(
            name='positionnode',
            options={'verbose_name': 'координаты Ноды', 'verbose_name_plural': 'координаты Ноды'},
        ),
        migrations.RemoveField(
            model_name='datanode',
            name='bubble_id',
        ),
        migrations.RemoveField(
            model_name='datanode',
            name='data',
        ),
        migrations.RemoveField(
            model_name='positionnode',
            name='canvas',
        ),
        migrations.AddField(
            model_name='datanode',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='bubble.node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='positionnode',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='bubble.node'),
            preserve_default=False,
        ),
    ]