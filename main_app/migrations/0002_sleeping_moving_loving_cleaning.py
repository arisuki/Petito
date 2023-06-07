# Generated by Django 4.2.1 on 2023-06-07 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sleeping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('sleep', models.CharField(choices=[('sleep1', 'take a nap')], default='sleep1', max_length=6)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Moving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('move', models.CharField(choices=[('love1', 'play fetch'), ('love3', 'go for a walk')], default='love1', max_length=6)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Loving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('love', models.CharField(choices=[('love1', 'give a hug'), ('love2', 'give kisses')], default='love1', max_length=6)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('clean', models.CharField(choices=[('clean1', 'clean poop'), ('clean2', 'bathe')], default='clean1', max_length=6)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
            ],
        ),
    ]
