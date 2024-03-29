# Generated by Django 3.1.1 on 2021-01-16 20:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customuser_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
