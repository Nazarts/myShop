# Generated by Django 4.1.3 on 2022-12-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_productitem_hover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='hover_img',
            field=models.FileField(null=True, upload_to='', verbose_name='alter_image'),
        ),
    ]