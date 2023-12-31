# Generated by Django 4.2.6 on 2023-11-01 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=15)),
                ('is_verified', models.BooleanField(default=False)),
                ('cuisine', models.CharField(choices=[('indian', 'Indian'), ('italian', 'Italian'), ('chinese', 'Chinese'), ('japanese', 'Japanese'), ('american', 'American')], max_length=100)),
                ('veg_or_nonveg', models.CharField(choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian'), ('both', 'Both')], max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('user', models.ForeignKey(limit_choices_to={'user_type': 'foodprovider'}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
