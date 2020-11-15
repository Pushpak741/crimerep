# Generated by Django 2.2 on 2020-11-08 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_case_ward_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='case.CaseCategory'),
        ),
        migrations.AlterField(
            model_name='case',
            name='cyber_case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='case.CyberCaseCategories'),
        ),
        migrations.AlterField(
            model_name='case',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citizen.Citizen'),
        ),
        migrations.AlterField(
            model_name='case',
            name='ward_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='police.Ward'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='case.Case'),
        ),
        migrations.AlterField(
            model_name='witness',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='case.Case'),
        ),
    ]