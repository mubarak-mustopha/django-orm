# Generated by Django 4.0.10 on 2024-05-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restuarant_type',
            field=models.CharField(choices=[('IN', 'Indian'), ('CH', 'Chinese'), ('IT', 'Italian'), ('GK', 'Greek'), ('MX', 'Mexican'), ('FF', 'Fast Food'), ('OT', 'Other')], default='FF', max_length=2),
        ),
    ]