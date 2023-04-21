# Generated by Django 4.1.3 on 2022-12-14 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_productitem_hover_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItemImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_img', models.FileField(upload_to='', verbose_name='big_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.productitem')),
            ],
        ),
    ]