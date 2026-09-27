import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import mannwhitneyu

# Einlesen des Datensatzes
df = pd.read_csv('data/student-mat.csv', sep=";")

#print(df.describe())
#print(df.columns)

a = df['Dalc']
a_t = a.loc[df['sex'] == 'M']
a_f = a.loc[df['sex'] == 'F']

print(a_t)
print(a_f)
plt.boxplot([a_t, a_f])
plt.xticks(ticks=[1,2],labels=['Male', 'Female'])
plt.show()

s, p = mannwhitneyu(a_t, a_f)

print("test statistics:", s)
print("p-value", p)

#print([a_f, a_t])
#x = pd.crosstab(df['Dalc'],df['famsup'], normalize='index')
#x.plot.bar(rot=0)
#plt.show()
