# Generated by Django 3.2.7 on 2021-09-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_auto_20211001_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookbook',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
