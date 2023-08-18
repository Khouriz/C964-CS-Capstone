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

filepath = None
df = None

def BrowseForFile():
    pass

def DataPreprocessing():
    pass

def LogisticRegressionPrediction():
    if df is None:
        header = "No Imported Data"
        body = "You need to import data ot the application using Browse."
        PopUpHandler(header,body)

def PopUpHandler(header:str, body:str):
    popup = Toplevel()
    popup.title(header)

    label = Label(popup, text=body)
    label.pack(padx=20, pady=20)

    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack()
    popup.wait_window(popup)

#Create Tk window as set attributes
window = Tk()
window.title("Crazy Corp Credit Fraud Detection")
window.geometry("500x300")
window.resizable(height=False, width=False)
window.config(background="white")

#Set base buttons
exit_button = Button(window, text="Exit", background="red", command=exit)
browse_button = Button(window,text="Browse", command=BrowseForFile)
submit_button = Button(window, text="Submit", command=LogisticRegressionPrediction)

#Button locations
exit_button.place(x=460, y=260)
browse_button.place(x=400,y=260)
submit_button.place(x=340, y=260)

window.mainloop()

