# Generated by Django 4.0.1 on 2022-03-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_alter_card_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tags',
            field=models.CharField(max_length=255),
        ),
    ]