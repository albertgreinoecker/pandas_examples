
import pandas as pd
from matplotlib import pyplot as plt


# Einlesen des Datensatzes
df = pd.read_csv('/home/albert/Downloads/european_social_survey/ESS8e02.1_F1.csv', sep=",")

#print(df.describe())
print("Columns:", df.columns.values)
print("Nr. Entries:", len(df))

print (df.gndr.value_counts)  #1...Male 2...Female, 9...No Answer

#Umkodieren der Zahlenwerte zu Kategorien
df['gndr'] = pd.cut(df['gndr'], [0,1,2,9], labels=['Male', 'Female', 'No Answer'])
# Zur Überprüfung checken ob die gleiche Anzahl rauskommt wie oben
print (df.gndr.value_counts())

# Grafische Darstellung davon
df['gndr'].value_counts().plot(kind='bar')
plt.show()

# Auswahl von einer Gruppe
df_f = df.loc[df['gndr'] == 'Female']
print(df_f.head().gndr)

# Darstellung von Häufigkeiten
gndr_cntry = pd.crosstab(df['gndr'], df['cntry'])
# in Pycharm: Variablenansicht. Rechte Maustaste auf Variable => Vie as DataFrame liefert eine bessere Anzeige
print(gndr_cntry)




