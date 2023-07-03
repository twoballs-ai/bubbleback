# Generated by Django 4.2.2 on 2023-06-29 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0010_rename_bubblelist_canvas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edge_id', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bubble.canvas')),
            ],
            options={
                'verbose_name': 'Узлы',
                'verbose_name_plural': 'Узлы',
            },
        ),
    ]
