# Generated by Django 4.1.3 on 2022-12-07 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_productitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variation', related_query_name='product_variation', to='api.product'),
        ),
    ]