import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

print(df.describe())
print(df.columns)

ct_internet_higher = pd.crosstab(df['internet'], df['higher'])
print(ct_internet_higher)

ct_internet_higher_pct = pd.crosstab(df['internet'], df['higher'], normalize='all')
print(ct_internet_higher_pct)

sns.heatmap(ct_internet_higher, annot=True, cmap="YlGnBu", fmt='d')
plt.show()

chi, p, dof, expected = chi2_contingency(ct_internet_higher)
print ("Chi:",chi)
print ("p:", p)
print ("dof" ,dof)
print ("expected",expected)

sns.heatmap(ct_internet_higher, annot=False, cmap="YlGnBu")

sns.heatmap(ct_internet_higher, annot=ct_internet_higher, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sns.heatmap(ct_internet_higher, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()


ex = pd.DataFrame(expected)
print(ex)


