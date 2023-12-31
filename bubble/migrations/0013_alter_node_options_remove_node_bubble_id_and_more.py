# Generated by Django 4.2.2 on 2023-06-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0012_alter_edge_canvas_alter_node_canvas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={},
        ),
        migrations.RemoveField(
            model_name='node',
            name='bubble_id',
        ),
        migrations.RemoveField(
            model_name='node',
            name='label',
        ),
        migrations.RemoveField(
            model_name='node',
            name='link',
        ),
        migrations.RemoveField(
            model_name='node',
            name='posX',
        ),
        migrations.RemoveField(
            model_name='node',
            name='posY',
        ),
        migrations.RemoveField(
            model_name='node',
            name='style',
        ),
        migrations.AlterField(
            model_name='node',
            name='canvas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canvas_nodes', to='bubble.canvas'),
        ),
        migrations.CreateModel(
            name='PositionNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posX', models.IntegerField()),
                ('posY', models.IntegerField()),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='bubble.canvas')),
            ],
            options={
                'verbose_name': 'Ноды',
                'verbose_name_plural': 'Ноды',
            },
        ),
        migrations.CreateModel(
            name='DataNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bubble_id', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='bubble.canvas')),
            ],
            options={
                'verbose_name': 'Ноды',
                'verbose_name_plural': 'Ноды',
            },
        ),
    ]
