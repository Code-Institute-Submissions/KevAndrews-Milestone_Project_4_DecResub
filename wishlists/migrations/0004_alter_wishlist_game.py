# Generated by Django 3.2.9 on 2022-01-01 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_game'),
        ('wishlists', '0003_auto_20220101_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.game'),
        ),
    ]
