import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

#print(df.describe())
#print(df.columns)

a = df['Walc']
a_t = a.loc[df['famsup'] == 'yes']
a_f = a.loc[df['famsup'] == 'no']

print(a_t)
print(a_f)
plt.boxplot([a_t, a_f])
plt.xticks(ticks=[1,2],labels=['Ja', 'Nein'])
plt.show()

s, p = mannwhitneyu(a_t, a_f)

print("test statistics:", s)
print("p-value", p)

#print([a_f, a_t])
x = pd.crosstab(df['Walc'],df['famsup'], normalize='index')
x.plot.bar(rot=0)
plt.show()