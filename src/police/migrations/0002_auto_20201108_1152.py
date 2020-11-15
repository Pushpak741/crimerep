# Generated by Django 2.2 on 2020-11-08 06:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='police.Ward'),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='police.Ward'),
        ),
        migrations.AlterField(
            model_name='police',
            name='ward',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='police.Ward'),
            preserve_default=False,
        ),
    ]