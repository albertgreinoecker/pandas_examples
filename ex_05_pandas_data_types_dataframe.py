import pandas as pd
import numpy as np


# einfaches Errzeugen eines Data Frame
data = [[1, 'a'], [2, 'b'] , [ 3, 'c']]
df = pd.DataFrame(data, columns = ['zahlen', 'buchstaben'])
print (df)

# Holen der Zeilenindices
print ("index:" , df.index[0])


# Es kann natürlich wieder ein Index vergeben werden
df = pd.DataFrame(data, columns = ['zahlen', 'buchstaben'], index = ['z1', 'z2', 'z3'])
print(df)

# Erzeugen eines Dataframe aus einem Dictionary

data = {'Name':['Hubert', 'Herbert', 'Franz'],
'Age':[28,42, 12]}
df= pd.DataFrame(data)
print(df)

# Erzeugen aus Series

d = {'spalte1' : pd.Series([1, 2, 3], index=['x', 'y', 'z']),
    'spalte2' : pd.Series([1, 2, 3, 4], index=['x', 'y', 'z', 'a'])}
df = pd.DataFrame(d)
print (df)

print (df['spalte1']) # Nan 1.0 2.0 3.0
print (df['spalte1'][1]) # 1.0

# Hinzufügen einer Neuen Spalte geht auch über den Namen

df['spalte3'] = pd.Series([100,200,300],index=['a','x','y'])
print (df)

del df['spalte1']
print(df)

# Auswahl der Zeilen mit loc
print ('loc:')
print(df.loc['a'])
print(df.loc[['a','x']])


# Auswahl der Zeilen über die Position (en) mit iloc:
print ('iloc:')
print(df.iloc[0]) # Auswahl der ersten Zeile
print(df.iloc[0:2]) # Auswahl der Zeilen 1 und 2

# Zeilen hinzufügen mit append:
df2 = pd.DataFrame([[70., 80.], [71., 81.]] , columns=['spalte2', 'spalte3'])
df = df.append(df2) # Die Spalten werden gemachtched
print (df)

# Löschen von Spalten über den Index mit drop

df = df.drop('a')
print(df)
df = df.drop(df.index[0]) # Zuerst den Zeilennamen an der Stelle 0 holen
df = df.drop(df.index[1:3]) # Auch hier kann der : - Operator angewandt werden
print(df)

print('axes:', df.axes)

# Anzahl der Zeilen:
print('size:', df.size)

# Übertragung in ein normales Array
print('values:', df.values)

print(df.head())
print(df.tail())