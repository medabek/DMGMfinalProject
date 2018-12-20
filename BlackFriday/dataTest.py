# from pydoc import help
# from scipy.stats.stats import pearsonr
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import pandas as pd
# from pandas import DataFrame
# import warnings
# warnings.filterwarnings("ignore", category=FutureWarning)
# from sklearn.ensemble import RandomForestRegressor

import pandas as pd
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rcsetup
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import string


class Data(object):

    @staticmethod
    def data_min(ar):

        #print("here")
        dataset = pd.read_csv("/home/mederbek/Desktop/DM/new_sample.csv")
        X = dataset.drop('Marital_Status', axis=1)
        y = dataset['Marital_Status']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        classifier = DecisionTreeClassifier()
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        print(y_pred)
        y_new = classifier.predict(ar)
        return y_new




