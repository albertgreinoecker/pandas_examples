import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency
import statsmodels.api as sm

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

print(df.describe())
print(df.columns)

ct_sex_higher = pd.crosstab(df['sex'], df['higher'])
print(ct_sex_higher)

ct_sex_higher_pct = pd.crosstab(df['sex'], df['higher'], normalize='all')
print(ct_sex_higher_pct)

# sns.heatmap(ct_sex_higher, annot=True, cmap="YlGnBu", fmt='d')
# plt.show()


chi, p, dof, expected = chi2_contingency(ct_sex_higher)
print ("Chi:",chi)
print ("p:", p)
print ("dof" ,dof)
print ("expected",expected)

sns.heatmap(ct_sex_higher, annot=False, cmap="YlGnBu")
sns.heatmap(ct_sex_higher, annot=ct_sex_higher, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sns.heatmap(ct_sex_higher, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

print (type(ct_sex_higher), type(expected))
ex = pd.DataFrame(expected)
print(ex)
both = pd.concat([ct_sex_higher, ex])
print(both)