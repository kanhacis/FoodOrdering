# Generated by Django 4.2.6 on 2023-11-01 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurant_address'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rating',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.review'),
        ),
    ]
