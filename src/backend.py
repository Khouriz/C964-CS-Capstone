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
import warnings

#3rd Party Libraries
import joblib
import pandas as pd
from sklearn.preprocessing import RobustScaler

warnings.filterwarnings("ignore")

class Backend():
    def __init__(self):
        self.out_path = "./src/output/output.csv"
        self.LRMODEL = joblib.load("./src/LogisticRegressionModel.joblib")
        self.df = None
        self.scaled_df = None
        self.predictions = None

    def data_importation(self, path:str):
        self.df = pd.read_csv(path)
        self.data_preprocessing()

    def data_preprocessing(self):
        
        self.scaled_df = self.df.copy()
        rbst_scaler = RobustScaler()

        self.scaled_df['scaled_time'] =  rbst_scaler.fit_transform(self.df['Time'].values.reshape(-1,1))
        self.scaled_df['scaled_amount'] = rbst_scaler.fit_transform(self.df['Amount'].values.reshape(-1,1))

        self.scaled_df.drop(['Amount', 'Time'], axis=1, inplace=True)

        scaled_amount = self.scaled_df['scaled_amount']
        scaled_time = self.scaled_df['scaled_time']

        self.scaled_df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)

        self.scaled_df.insert(0, 'scaled_time', scaled_time)
        self.scaled_df.insert(29, 'scaled_amount', scaled_amount)

    def data_prediction(self):
        self.predictions = self.LRMODEL.predict(self.scaled_df)
        self.data_exportation()
    
    def data_exportation(self):
        self.df['Class'] = self.predictions
        self.df.to_csv(self.out_path, index=False)