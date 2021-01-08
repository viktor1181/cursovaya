# Generated by Django 3.1.5 on 2021-01-08 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20210106_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='engine',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='engine', to='server.engines'),
        ),
    ]
