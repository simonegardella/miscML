# Series : vettori monodimensionali ad una dimensione
# DataFrame : metrice due dimensioni

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

miaserie = pd.Series([1,2,np.nan,4])
print (miaserie)
date = pd.date_range('20250101',periods=6)
persone = ['Mario','Sofia','Luigi','Genoveffa']

print (date)
mioDF = pd.DataFrame (np.random.random((6,4)),index = date,columns=persone )
plt.figure()

miaserie.plot()
plt.show()

print (mioDF)

iris = pd.read_csv('iris.csv',sep=',')



dizionario ={'A':1.0,
             'B':miaserie,
             'C':np.array([5]*4,dtype=np.uint8)}

dataframeDaDizionario = pd.DataFrame(dizionario)
print (dataframeDaDizionario)   
