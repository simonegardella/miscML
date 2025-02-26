import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



sns.set_style('whitegrid')

tips = sns.load_dataset('tips')

corr = tips.corr()


sns.heatmap(corr,cmap='coolwarm',annot=True)
plt.show()
