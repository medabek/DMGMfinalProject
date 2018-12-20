from django.db import models
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Create your models here.


class Person(models.Model):
    gender = models.IntegerField()
    age = models.IntegerField()
    occupation = models.IntegerField()
    city_category = models.IntegerField()
    stay_years = models.IntegerField()
    #marital = models.IntegerField()
    product_id = models.IntegerField()
    purchase = models.IntegerField()
