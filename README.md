# C964-CS-Capstone

## Introduction

> *You can skip to the [Table of Contents](#table%20of%20contents).*

Welcome to my CS Capstone project for WGU C964. The scenarios used for the conceptions of this project was the following:

>*You as the developer have been given the task to create a software application, in your preferred language, that solves a business problem.*

This business problem was something we as students needed to address on our own. Some of the requirements for the project were:

1. Must include a machine learning model
2. Must provide a GUI (can be CLI, desktop application, web-app)
3. Must provide 3 different views for output
4. Must improve upon the current systems implemented at the business of your choice

So with those requirements in mind and the ability to create a fictional business with a technical need for this product I came up with the following:

>*Here at Crazy Corporation we offer financial services to our customers. The most prominent service is credit cards, and the largest threat to this service is fraud. For this project I will use Python to create an application that will take data provided from our analysts, train a machine learning model for more timely identification of  fraud, and enhance our current method of fraud detection that the business currently has.*

This is a rough overview as a majority of the official documentation took place in a series of reports.

The dataset mentioned was pulled from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and is anonymized real credit card data. Unfortunately I cannot provide you an accurate breakdown of the anonymized features.

The machine learning model's source code is located in the Jupyter notebook that is contained in the project. This notebook outlines the steps taken for data exploration and cleaning, the training of the actual model (Logistic Regression), and the testing and outputting of the model for use in the desktop application.

The core portion of the application that will be used by most users is the desktop application. The rest of the README will focus directly on setting up the environment necessary for running the desktop application.
## Table of Contents

1) [Requirements](#requirements)
2) [Installation](#installation)
3) [Configuration](#configuration)
4) [Maintenance](#maintenance)
## Requirements

- A machine that can run: 
	- Python 3.11.x
	- Visual Studio Code
- Must have third-party libraries:
	- matplotlib
	- seaborn
	- pandas
	- scikit-learn
	- jupyterlab (optional)

***Will go over installation below!***
## Installation 

>*All instructions below are for a Windows 10 installation and may differ slightly for Linux and MacOS*

1) Install Visual Studio Code installer from [here](https://code.visualstudio.com/). If you already have it installed then you can skip this steps and the sub-steps below and look at step 2.
	1) Run the executable that was downloaded
	2) Follow default installation instructions. 
2) Download the latest Python 3.11.x installer from [here](https://www.python.org/downloads/) (select the interpreter that works with your CPU architecture and platform)
	1) Run the installer and select the checkbox for adding Python to PATH 
	2) Click “Install Now” option and close installer once finished 
3) Download `C964-CS-Capstone.zip` from GitHub. 
	1) Extract `C964-CS-Capstone.zip` into a directory of your choice. (This will take some time)
4) Navigate to “Terminal” on the top of the window 
	1) Select “New Terminal” 
	2) Enter the each command below: 

>*These install the third party libraries needed by the project and the associated dependencies each library may have*

```
pip install matplotlib
``` 

 ```
pip install seaborn
``` 

```
pip install pandas
```

```
pip install scikit-learn
```

> *The below line is only for those who wish to visualize the Jupyter notebook containing information on the machine learning model*

``` 
pip install jupyterlab
```

## Configuration

1) Open Visual Studio Code and navigate to “File” in the top right (make sure that the window is full screen) 
2) Select “Open Folder…” 
3) Navigate to the directory the extraction is saved 
4) Select `C964-CS-Capstone` folder and open it 
5) Expand `src` directory and click on `main.py`
6) In the bottom right it should say Python 3.11.x 
	1) If it does not:
		1) Click on select interpreter 
			1) A drop down should appear at the top on the window
		2) Select the line that says Python 3.11.x 64-bit 
7) In the top right click the play symbol  
8) After the GUI loads press browse and select your data that is formatted like `example_data_formatting.csv` 
9) Click Submit :
	1) Bar Chart tab should populate with a count of non-fraud (0) and fraud (1) found amongst the input data 
	2) Pie Chart tab populates with the percentages of both non-fraud (0) and fraud (1) found amongst the input data 
10) Navigate to the output directory in the file explorer
	1) open `output.csv` to see predictions associated with the respective transaction data

>Note: The configuration is solely for a user that means to use the application as intended for a business oriented audience and not a technical audience.
## Maintenance

There are no active plans to develop this project further than what is already here. 
