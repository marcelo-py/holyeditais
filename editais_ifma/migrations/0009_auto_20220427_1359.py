# Generated by Django 2.2.3 on 2022-04-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editais_ifma', '0008_auto_20220427_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menssagens',
            name='edital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='editais_ifma.Edital', verbose_name='Edital'),
        ),
    ]