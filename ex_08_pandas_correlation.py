import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import spearmanr, pearsonr
import statsmodels.api as sm

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

print(df.describe())
print(df.columns)

df_corr = df[['G3', 'Dalc']] #'G1','G2',
print(df_corr)

df_cross = pd.crosstab(df_corr['G3'], df_corr['Dalc'])

sns.heatmap(df_cross, annot=True, cmap="YlGnBu")
plt.show()

c = df_corr.corr(method ='spearman') #pearson
print(c)

# Wenn man auch einen p-Wert haben möchte
corr, p = spearmanr(df_corr['G3'], df_corr['Dalc'])
print("corr: %.6f" % corr)
print("p-value: %.6f" % p)

