# Generated by Django 4.0.1 on 2022-03-02 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='insights.tag'),
        ),
    ]
