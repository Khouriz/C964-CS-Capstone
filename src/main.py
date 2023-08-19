#! ./venv/Scripts/python
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
from tkinter import filedialog
import os, sys

#Custom Libraries
from backend import Backend



backend_handler = Backend()

def BrowseForFile():
    path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="Select a File",
                                      filetypes=(("CSV Files", "*.csv"),)
                                      )
    backend_handler.data_importation(path)
   

def LogisticRegressionPrediction():
    if backend_handler.scaled_df is None:
        header = "No Imported Data"
        body = "You need to import data ot the application using Browse."
        PopUpHandler(header,body)
    backend_handler.data_prediction()

def PopUpHandler(header:str, body:str):
    #Create popup and set correct settings. Disables application when popup is active.
    popup = Toplevel()
    popup.title(header)
    popup.resizable(height=False, width=False)
    popup.grab_set()
   
    #Label for bodytext. Setting the label's window to popup.
    label = Label(popup, text=body)
    label.pack(padx=20, pady=20)

    #Creates new button for closing the popup and destroys it
    #enabling application to perform agains
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

