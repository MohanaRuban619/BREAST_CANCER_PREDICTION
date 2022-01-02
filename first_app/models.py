from django.db import models
class Input(models.Model):
    radius_mean = models.IntegerField()
    texture_mean = models.IntegerField()
    perimeter_mean = models.IntegerField()
    area_mean = models.IntegerField()
    smoothness_mean = models.IntegerField()
    compactness_mean = models.IntegerField()
    concavity_mean = models.IntegerField()
    concave_points_mean = models.IntegerField()
    symmetry_mean = models.IntegerField()
    fractal_dimension_mean = models.IntegerField()
    radius_se = models.IntegerField()
    texture_se = models.IntegerField()
    perimeter_se = models.IntegerField()
    area_se = models.IntegerField()
    smoothness_se = models.IntegerField()
    compactness_se = models.IntegerField()
    concavity_se = models.IntegerField()
    concave_points_se = models.IntegerField()
    symmetry_se = models.IntegerField()
    fractal_dimension_se = models.IntegerField()
    radius_worst = models.IntegerField()
    texture_worst = models.IntegerField()
    perimeter_worst = models.IntegerField()
    area_worst = models.IntegerField()
    smoothness_worst = models.IntegerField()
    compactness_worst = models.IntegerField()
    concavity_worst = models.IntegerField()
    concave_points_worst = models.IntegerField()
    symmetry_worst = models.IntegerField()
    fractal_dimension_wors = models.IntegerField()


    
    def __str__(self):
        return super().__str__()

# Create your models here.
