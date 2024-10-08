# Generated by Django 5.0.6 on 2024-10-04 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherLinkStationMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weatherlink_station_id', models.PositiveIntegerField(help_text='Select the WeatherLink Station ID', unique=True, verbose_name='WeatherLink Station ID')),
                ('last_imported', models.DateTimeField(blank=True, null=True, verbose_name='Last Imported')),
                ('station', models.OneToOneField(help_text='Station to link', on_delete=django.db.models.deletion.CASCADE, to='core.station', verbose_name='Station')),
            ],
            options={
                'verbose_name': 'WeatherLink Station Link',
                'verbose_name_plural': 'WeatherLink Stations Link',
            },
        ),
        migrations.CreateModel(
            name='WeatherLinkStationDataStructureMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_conditions_data_structure_type', models.CharField(blank=True, null=True)),
                ('station_mapping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data_structure_mapping', to='wis2box_adl_weatherlink_v2_plugin.weatherlinkstationmapping', verbose_name='Station Mapping')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherLinkStationParameterMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weatherlink_parameter', models.CharField(max_length=255, verbose_name='WeatherLink Parameter')),
                ('data_structure_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weatherlink_station_parameter_mappings', to='wis2box_adl_weatherlink_v2_plugin.weatherlinkstationdatastructuremapping', verbose_name='Station Mapping')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dataparameter', verbose_name='Parameter')),
            ],
            options={
                'verbose_name': 'WeatherLink Station Parameter Mapping',
                'verbose_name_plural': 'WeatherLink Station Parameter Mapping',
            },
        ),
        migrations.AddConstraint(
            model_name='weatherlinkstationparametermapping',
            constraint=models.UniqueConstraint(fields=('data_structure_mapping', 'parameter'), name='unique_weatherlink_station_mapping_parameter'),
        ),
    ]
