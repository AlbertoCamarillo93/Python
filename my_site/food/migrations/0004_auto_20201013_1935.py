# Generated by Django 3.1.1 on 2020-10-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
