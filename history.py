# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

##---(Sat Sep 16 10:07:41 2017)---
runfile('C:/Users/pc/.spyder-py3/temp.py', wdir='C:/Users/pc/.spyder-py3')
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
print ("Hello Spider Dai Nguyen")import numpy as np import matplotlib.pyplot as pltimport pandas as pd #lib to import and manage dataset
clear
clc
clear
print ("Hello Spider Dai Nguyen")import numpy as np import matplotlib.pyplot as pltimport pandas as pd #lib to import and manage dataset
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
X
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
Y
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
clear
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
X
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
X
X[5;1:3]
X[1:5;1:3]
X[1:5,1:3]
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
X
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
X
runfile('C:/Users/pc/Machine Learning/temp.py', wdir='C:/Users/pc/Machine Learning')
clear
import numpy as np import matplotlib.pyplot as pltimport pandas as pd #lib to import and manage datasetdataset=pd.read_csv('Data.csv')X=dataset.iloc[:,:-1].values #select all column except the last columny=dataset.iloc[:,3].values#Taking care of missing datafrom sklearn.preprocessing import Imputerimputer=Imputer(missing_values='NaN',strategy="mean", axis=0)imputer=imputer.fit(X[:,1:3])X[:,1:3]=imputer.transform(X[:,1:3])#Categorical Datafrom sklearn.preprocessing import LabelEncoder, OneHotEncoderlabelencoder_X=LabelEncoder();X[:,0]=labelencoder_X.fit_transform(X[:,0])onehotencoder=OneHotEncoder(categorical_features=[0]);X=onehotencoder.fit_transform(X).toarray()labelencoder_y=LabelEncoder();y=labelencoder_y.fit_transform(y)#splitting  the dataset into Training set and Test setfrom sklearn.cross_validation import train_test_splitX_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScalersc_X=StandardScaler();X_train=sc_X.fit_transform(X_train)X_test=sc_X.transform(X_test)

##---(Tue Sep 26 20:19:51 2017)---
print ("Hello Spider Dai Nguyen")
runfile('C:/Users/pc/.spyder-py3/temp.py', wdir='C:/Users/pc/.spyder-py3')