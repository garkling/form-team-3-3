# Generated by Django 3.1.1 on 2021-01-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
