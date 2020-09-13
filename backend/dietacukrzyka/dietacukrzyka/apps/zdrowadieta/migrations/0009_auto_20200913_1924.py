# Generated by Django 2.2.3 on 2020-09-13 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zdrowadieta', '0008_client_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='client',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbs',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Carbs'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fats',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Fats'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Weight'),
        ),
    ]
