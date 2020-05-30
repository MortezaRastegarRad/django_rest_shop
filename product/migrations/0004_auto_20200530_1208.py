# Generated by Django 3.0.5 on 2020-05-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images_path',
            field=models.CharField(editable=False, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
