# Generated by Django 4.2.7 on 2023-11-02 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
        ('order', '0005_remove_order_delivery_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.delivery'),
        ),
    ]
