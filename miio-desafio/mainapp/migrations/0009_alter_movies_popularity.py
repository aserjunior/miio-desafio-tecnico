# Generated by Django 4.2.5 on 2023-09-10 04:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_movies_vote_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
