# Generated by Django 4.2.2 on 2023-06-30 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0021_remove_datanode_node_remove_edge_canvas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='canvas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='bubble.canvas'),
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edges', to='bubble.canvas')),
            ],
            options={
                'verbose_name': 'Ноды',
                'verbose_name_plural': 'Ноды',
            },
        ),
    ]
