import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from joblib import dump,load
loaded_model = load("final_SVM_model.sav")
dataset = pd.read_csv('Live.csv')
result = loaded_model.predict(dataset)
#print result[0]
pax = result[0]
if pax == 1:
    print "anamolous"
else:
    print "normal"

p = open("Result.txt", "w")
p.write(str(pax))

