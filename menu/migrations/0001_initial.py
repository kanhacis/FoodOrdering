# Generated by Django 4.2.6 on 2023-11-01 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian')], max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image1', models.ImageField(upload_to='menu_images/')),
                ('image2', models.ImageField(blank=True, upload_to='menu_images/')),
                ('image3', models.ImageField(blank=True, upload_to='menu_images/')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.review')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]