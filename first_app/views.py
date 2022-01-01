
from django import forms
from django.db import models
from .forms import InputForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse, response
from rest_framework.parsers import JSONParser
from .models import Input
from .serializer import InputSerializers
from sklearn.datasets import load_breast_cancer
import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.shortcuts import render,redirect
from django.contrib import messages
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

class Inputview(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializers
  
def FormView(request):
    return render(request,'forms.html',{})
def status(request):
    file = joblib.load(open("first_app/b_c.svc","rb"))
    clas = file
    lis = []
    lis.append(request.GET["radius_mean"])
    lis.append(request.GET["texture_mean"])
    lis.append(request.GET["perimeter_mean"])
    lis.append(request.GET["area_mean"])
    lis.append(request.GET["smoothness_mean"])
    lis.append(request.GET["compactness_mean"])
    lis.append(request.GET["concavity_mean"])
    lis.append(request.GET["concave_points_mean"])
    lis.append(request.GET["symmetry_mean"])
    lis.append(request.GET["fractal_dimension_mean"])
    lis.append(request.GET["radius_se"])
    lis.append(request.GET["texture_se"])
    lis.append(request.GET["perimeter_se"])
    lis.append(request.GET["area_se"])
    lis.append(request.GET["smoothness_se"])
    lis.append(request.GET["compactness_se"])
    lis.append(request.GET["concavity_se"])
    lis.append(request.GET["concave_points_se"])
    lis.append(request.GET["symmetry_se"])
    lis.append(request.GET["fractal_dimension_se"])
    lis.append(request.GET["radius_worst"])
    lis.append(request.GET["texture_worst"])
    lis.append(request.GET["perimeter_worst"])
    lis.append(request.GET["area_worst"])
    lis.append(request.GET["smoothness_worst"])
    lis.append(request.GET["compactness_worst"])
    lis.append(request.GET["concavity_worst"])
    lis.append(request.GET["concave_points_worst"])
    lis.append(request.GET["symmetry_worst"])
    lis.append(request.GET["fractal_dimension_wors"])
    

    answer  = clas.predict([lis])
    return render(request,'status.html',{"answer":answer}) 

# Create your views here.




            # radius_mean = form.cleaned_data["radius_mean"]
            # radius_mean = form.cleaned_data["radius_mean"]
            # perimeter_mean = form.cleaned_data["perimeter_mean"]
            # area_mean = form.cleaned_data["perimeter_mean"]
            # smoothness_mean = form.cleaned_data["perimeter_mean"]
            # compactness_mean = form.cleaned_data["perimeter_mean"]
            # concavity_mean = form.cleaned_data["perimeter_mean"]
            # concave_points_mean = form.cleaned_data["perimeter_mean"]
            # symmetry_mean = form.cleaned_data["perimeter_mean"]
            # fractal_dimension_mean = form.cleaned_data["perimeter_mean"]
            # radius_se = form.cleaned_data["perimeter_mean"]
            # texture_se = form.cleaned_data["perimeter_mean"]
            # perimeter_se = form.cleaned_data["perimeter_mean"]
            # area_se = form.cleaned_data["perimeter_mean"]
            # smoothness_se = form.cleaned_data["perimeter_mean"]
            # compactness_se = form.cleaned_data["perimeter_mean"]
            # concavity_se = form.cleaned_data["perimeter_mean"]
            # concave_points_se = form.cleaned_data["perimeter_mean"]
            # symmetry_se = form.cleaned_data["perimeter_mean"]
            # fractal_dimension_se = form.cleaned_data["perimeter_mean"]
            # radius_worst = form.cleaned_data["perimeter_mean"]
            # texture_worst = form.cleaned_data["perimeter_mean"]
            # perimeter_worst = form.cleaned_data["perimeter_mean"]
            # area_worst = form.cleaned_data["perimeter_mean"]
            # smoothness_worst = form.cleaned_data["perimeter_mean"]
            # compactness_worst = form.cleaned_data["perimeter_mean"]
            # concavity_worst = form.cleaned_data["perimeter_mean"]
            # concave_points_worst = form.cleaned_data["perimeter_mean"]
            # symmetry_worst = form.cleaned_data["perimeter_mean"]
            # fractal_dimension_wors = form.cleaned_data["perimeter_mean"]
