# Generated by Django 3.2.7 on 2021-10-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0006_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subtitle_down',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='subtitle_up',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
