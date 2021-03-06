# Generated by Django 4.0 on 2021-12-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius_mean', models.IntegerField()),
                ('texture_mean', models.IntegerField()),
                ('perimeter_mean', models.IntegerField()),
                ('area_mean', models.IntegerField()),
                ('smoothness_mean', models.IntegerField()),
                ('compactness_mean', models.IntegerField()),
                ('concavity_mean', models.IntegerField()),
                ('concave_points_mean', models.IntegerField()),
                ('symmetry_mean', models.IntegerField()),
                ('fractal_dimension_mean', models.IntegerField()),
                ('radius_se', models.IntegerField()),
                ('texture_se', models.IntegerField()),
                ('perimeter_se', models.IntegerField()),
                ('area_se', models.IntegerField()),
                ('smoothness_se', models.IntegerField()),
                ('compactness_se', models.IntegerField()),
                ('concavity_se', models.IntegerField()),
                ('concave_points_se', models.IntegerField()),
                ('symmetry_se', models.IntegerField()),
                ('fractal_dimension_se', models.IntegerField()),
                ('radius_worst', models.IntegerField()),
                ('texture_worst', models.IntegerField()),
                ('perimeter_worst', models.IntegerField()),
                ('area_worst', models.IntegerField()),
                ('smoothness_worst', models.IntegerField()),
                ('compactness_worst', models.IntegerField()),
                ('concavity_worst', models.IntegerField()),
                ('concave_points_worst', models.IntegerField()),
                ('symmetry_worst', models.IntegerField()),
                ('fractal_dimension_wors', models.IntegerField()),
            ],
        ),
    ]
