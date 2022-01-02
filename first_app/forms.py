from django import forms
from .models import Input

class InputForm(forms.ModelForm):
    class Meta:
            model = Input
            fields = "__all__"

    radius_mean = forms.IntegerField()
    texture_mean = forms.IntegerField()
    perimeter_mean = forms.IntegerField()
    area_mean = forms.IntegerField()
    smoothness_mean = forms.IntegerField()
    compactness_mean = forms.IntegerField()
    concavity_mean = forms.IntegerField()
    concave_points_mean = forms.IntegerField()
    symmetry_mean = forms.IntegerField()
    fractal_dimension_mean = forms.IntegerField()
    radius_se = forms.IntegerField()
    texture_se = forms.IntegerField()
    perimeter_se = forms.IntegerField()
    area_se = forms.IntegerField()
    smoothness_se = forms.IntegerField()
    compactness_se = forms.IntegerField()
    concavity_se = forms.IntegerField()
    concave_points_se = forms.IntegerField()
    symmetry_se = forms.IntegerField()
    fractal_dimension_se = forms.IntegerField()
    radius_worst = forms.IntegerField()
    texture_worst = forms.IntegerField()
    perimeter_worst = forms.IntegerField()
    area_worst = forms.IntegerField()
    smoothness_worst =forms.IntegerField()
    compactness_worst = forms.IntegerField()
    concavity_worst = forms.IntegerField()
    concave_points_worst = forms.IntegerField()
    symmetry_worst = forms.IntegerField()
    fractal_dimension_wors = forms.IntegerField()