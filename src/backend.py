#! ./venv/Scripts/python
"""
Backend.py defines the class Backend, 
This class is used to manage all the backend aspects of the application.
"""

__author__ = "Andrew Zulfa"
__credits__ = ["Andrew Zulfa"]
__version__ = "1.0.1"
__maintainer__ = "Andrew Zulfa"
__email__ = "azulfa@wgu.edu"
__status__ = "Devlopment"

#Native Libraries
import os
import sys

#3rd Party Libraries
import joblib
import pandas as pd

#Custom Libraries

class Backend():
    def __init__(self):
        self.LRMODEL = joblib.load("./src/LogisticRegressionML/LogisticRegressionModel.joblib")
        self.filepath = None
        self.df = None
        self.scaled_df = None
        self.predictions = None

    def data_importation(self, path):
        self.filepath = path

    def data_preprocessing(self):
        pass

    def data_prediction(self):
        pass