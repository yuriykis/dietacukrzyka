# Generated by Django 2.2.3 on 2020-09-14 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zdrowadieta', '0013_auto_20200913_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zdrowadieta.Menu')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zdrowadieta.Recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='MenuRecipe',
        ),
    ]
