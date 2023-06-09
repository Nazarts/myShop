# Generated by Django 4.1.3 on 2022-12-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('category_img', models.FileField(upload_to='', verbose_name='categories/')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='FilterModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification_value', models.CharField(max_length=255)),
                ('filter_modification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.filtermodification')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=8)),
                ('item_img', models.FileField(upload_to='', verbose_name='item_image/')),
                ('qty_in_stock', models.PositiveBigIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductFilterModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.modificationvalue')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productitem')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('product_img', models.FileField(upload_to='', verbose_name='product_image/')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
    ]
