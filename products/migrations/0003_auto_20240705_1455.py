# Generated by Django 3.2.12 on 2024-07-05 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
