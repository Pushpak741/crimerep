# Generated by Django 2.2 on 2020-11-08 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20171210_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='case.Case'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='police.Police'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='citizen.Citizen'),
        ),
    ]
