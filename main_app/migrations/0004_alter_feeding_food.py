# Generated by Django 4.2.1 on 2023-06-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_moving_move'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='food',
            field=models.CharField(choices=[('food1', 'feed burger'), ('food2', 'feed kale soup'), ('food3', 'feed donut')], default='food1', max_length=6),
        ),
    ]
