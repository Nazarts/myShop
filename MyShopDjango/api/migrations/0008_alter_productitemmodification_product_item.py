# Generated by Django 4.1.3 on 2022-12-07 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_productitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitemmodification',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_modification', to='api.productitem'),
        ),
    ]