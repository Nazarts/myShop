# Generated by Django 4.1.3 on 2022-12-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_productitem_item_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='hover_img',
            field=models.FileField(null=True, upload_to='', verbose_name='item_image'),
        ),
    ]