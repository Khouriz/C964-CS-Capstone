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
from tkinter import filedialog, ttk
import os

#3rd Party Libraries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns

#Custom Libraries
from backend import Backend

#Constants
HEADERS = ['Time','Amount', 'Class']

#created a Backend object to handle everything not in the perview of the frontend gui
backend_handler = Backend()

def BrowseForFile():
    #Uses native windows file explorer to find correct file
    path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="Select a File",
                                      filetypes=(("CSV Files", "*.csv"),)
                                      )
    #imports the data into the backend_handler
    backend_handler.data_importation(path)
   

def LogisticRegressionPrediction():
    #if there is no data that is loaded then an error is shown to the user explaining the issue.
    if backend_handler.scaled_df is None:
        header = "No Imported Data"
        body = "You need to import data ot the application using Browse."
        PopUpHandler(header,body)
    #predicts on the data that is loaded.
    backend_handler.data_prediction()
    BarTabCreation()
    PieTabCreation()


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

def BarTabCreation():
    fig = Figure(figsize=(5,4))
    ax = fig.add_subplot()
    sns.countplot(data=backend_handler.df, x="Class", ax=ax)
    ax.set_xlabel("Non-Fraud vs. Fraud")
    ax.set_ylabel("Count")
    bar_canvas = FigureCanvasTkAgg(fig,master=bar_tab)
    bar_canvas.get_tk_widget().pack(fill=BOTH, expand=True)

def PieTabCreation():
    fig = Figure(figsize=(5,4))
    ax = fig.add_subplot()
    counts = backend_handler.df["Class"].value_counts()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%' ,colors = sns.color_palette("pastel"), startangle=120)
    pie_canvas = FigureCanvasTkAgg(fig, master=pie_tab)
    pie_canvas.get_tk_widget().pack(fill=BOTH, expand=True)

#Create Tk window as set attributes
window = Tk()
window.title("Crazy Corp Credit Fraud Detection")
window.geometry("600x500")
window.resizable(height=False, width=False)
window.config(background="white")

#tab settings
tab_handler = ttk.Notebook(window)
tab_handler.pack(expand=1, fill="both")

#Tab #1
bar_tab = ttk.Frame(tab_handler)
tab_handler.add(bar_tab, text="Bar Chart")

#Tab #2
pie_tab = ttk.Frame(tab_handler)
tab_handler.add(pie_tab, text="Pie Chart")

#Set base buttons
exit_button = Button(window, text="Exit", background="red", command=exit)
browse_button = Button(window,text="Browse", command=BrowseForFile)
submit_button = Button(window, text="Submit", command=LogisticRegressionPrediction)

#Button locations
exit_button.place(x=560, y=465)
browse_button.place(x=500,y=465)
submit_button.place(x=440, y=465)

window.mainloop()

