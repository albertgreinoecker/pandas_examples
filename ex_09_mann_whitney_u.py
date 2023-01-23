import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

#print(df.describe())
#print(df.columns)

a = df['Walc']
a_m = a.loc[df['sex'] == 'M']
a_f = a.loc[df['sex'] == 'F']

plt.boxplot([a_m, a_f])
plt.xticks(ticks=[1,2],labels=['M', 'F'])
plt.show()

s, p = mannwhitneyu(a_m, a_f)

print("test statistics:", s)
print("p-value", p)

print([a_f, a_m])

x = pd.crosstab(df['Walc'],df['sex'], normalize='index')
x.plot.bar(rot=0)
plt.show()