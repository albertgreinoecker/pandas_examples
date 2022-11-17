import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

# Einlesen des Datensatzes
df = pd.read_csv('data/london_weather.csv')

print(df.columns)

df['mean_temp'].plot(title="Durchschnittstemperaturen")
plt.show()

df['day'] = (df.date % 100).astype('i')
df['month'] = (df.date % 10000 / 100).astype('i')
df['year'] = (df.date % 100000000 / 10000).astype('i')

y7 = df.loc[df['month'] == 7][['year','mean_temp']]
y7g = y7.groupby('year').mean()
y7g.plot(title="Mittelwerte im Juli")
plt.show()

years = y7g.index # Nach jeder Gruppierung steht die Gruppierungsvariable im Index
mean_temp = y7g.mean_temp
pred_years = range(2030, 2160)

model = sm.OLS(mean_temp, years).fit()  # Methode der kleinsten Quadrate
print(model.summary())
print(model.rsquared) # R-Quadrat als Maß wie gut das Modell ist
print(dir(model))
print("x", model.params[0]) # Das x der Formel. Normalerweise sollte noch ein zweiter Wert sein für die Konstante in y = ax + b
#print("fittedvalues", model.fittedvalues) # Die Punkte die auf der Regressionsgerade liegen
#print("resid:", model.resid) # Abweichungen von Punkten auf der geraden zu den Datenpunkten
predictions = model.predict(range(2000, 2030)) # Vorhersage der entsprechenden Temperaturwerte für die Jahre


#print(predictions)
plt.plot(range(2000, 2030), predictions)
plt.show()

reg =  model.predict(years)

plt.plot(y7g)
plt.plot(years, reg)
plt.xlim([1980, 2030])
plt.show()

#subplots
fig, axes = plt.subplots(nrows=2, ncols=2)

t1 = df.loc[df['month'] == 1][['year','mean_temp']].groupby('year').mean()
t4 = df.loc[df['month'] == 4][['year','mean_temp']].groupby('year').mean()
t9 = df.loc[df['month'] == 9][['year','mean_temp']].groupby('year').mean()
t12 = df.loc[df['month'] == 12][['year','mean_temp']].groupby('year').mean()

t1.plot(ax=axes[0,0], title="Jänner", legend=False);
t4.plot(ax=axes[0,1], title="April", legend=False);
t9.plot(ax=axes[1,0], title="September", legend=False);
t12.plot(ax=axes[1,1], title="Dezember", legend=False);

fig.tight_layout() # Dann überlagert sich die Ausgabe nicht
plt.show();