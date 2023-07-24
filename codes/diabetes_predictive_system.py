# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numpy as np


# save model file named as trainned_model.sav
filename='C:\\Users\\Anuruddha\\Desktop\\ML_projects\\2.Diabetes_Prediction\\codes\\trainned_model.sav'

# load the saved file

loaded_model = pickle.load(open(filename,'rb')) # read  as binary file

input_data = (8,183,64,0,0,23.3,0.672,32)

# changing the input data as numpy array

input_data_as_numpy_array = np.asarray(input_data)

# reshape the data

input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

# standarized the input data

#std_data = scaler.transform(input_data_reshape)

prediction  = loaded_model.predict(input_data_reshape)


if prediction[0] == 0:
    print('The persion is not diabetes')
else:
    print('The persion is diabetes')
    
