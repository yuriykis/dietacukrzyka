# Generated by Django 2.2.3 on 2020-11-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zdrowadieta', '0019_meal_is_eaten'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='physical_activity',
            field=models.IntegerField(default=0, verbose_name='Activity'),
        ),
    ]
