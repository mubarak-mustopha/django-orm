# Generated by Django 4.0.10 on 2024-06-06 18:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restuarant_type',
            new_name='restaurant_type',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='sale',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='core.restaurant'),
        ),
    ]
