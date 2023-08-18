#! ../venv python
"""
main.py starts a gui application that is used input and process credit transaction 
data and outputs those that are fraud.
"""

__author__ = "Andrew Zulfa"
__credits__ = ["Andrew Zulfa"]
__version__ = "1.0.1"
__maintainer__ = "Andrew Zulfa"
__email__ = "azulfa@wgu.edu"
__status__ = "Devlopment"

#Native Libraries
from tkinter import *
import os
import sys

#3rd Party Libraries
import joblib
import pandas as pd

#Custom Libraries


LRMODEL = joblib.load("./src/LogisticRegressionML/LogisticRegressionModel.joblib")

def BrowseForFile():
    pass

def LogisticRegressionPrediction():
    pass

#Create Tk window as set attributes
window = Tk()
window.title("Crazy Corp Credit Fraud Detection")
window.geometry("500x300")
window.config(background="white")

#Set base buttons
exit_button = Button(window, text="Exit", background="red", command=exit)


window.mainloop()

