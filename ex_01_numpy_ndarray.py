import numpy as np # Hat sich so eingebürgert dass als np importiert wird
a = np.array([1,2,3]) # So wird ein 1-dimensionales Array angelegt
print(a) # Ausgabe des Arrays
print(a.shape) # Wie viele Dimensionen
print(len(a.shape)) # Wie viele Werte auf den einzelnen Dimensionen
print(a.dtype) # Um welchen Datentyp handelt es sich?

#Hilfreiche Funktionen für die Erzeugung von Arrays

# Eindimensional
a1 = np.arange(10)
print("arange:", a1)

a11 = np.arange(10, 20, 0.5)
print("arange-bereich:" , a11)

a2 = np.linspace(1, 2, 5)
print("linspace:", a2)


a3 = np.ones(10)
print("ones:", a3)

a4 = np.zeros(10)
print("zeros:", a4)

a5 = np.random.rand(10)
print("random.rand:", a5)

a6 = np.random.randint(10,20,500)
print("random.randint:", a6)

#Mehrdimensional
ad1 = np.random.rand(3,2,4)
print("random:", ad1)


#####################################
# Datentypen:
#####################################

#Der Datentyp kann u.a. bei der Erzeugung gesetzt werden:
d1 = np.array([1,2,3],  dtype=complex)
print(d1)

d2 = np.array([1,2,3],  dtype=str)
print(d2)

d2 = d2.astype(int)
print(d2)

print(ad1)
ad1 = ad1.astype(str, copy=False, casting='safe')
print(ad1)



db = np.array(['1995-10-28 23:55', '2020-01-18 23:01'])
db = db.astype('M')
print(db)
db = db + (2 + 3*60)
print(db)

# Ändern der Dimension
dr1 = np.zeros(10)
dr1 = dr1.reshape(2,5)
print(dr1)


#################################
# Rechenoperationen

r1 = np.arange(10) * 10;
print(r1[1:3])

#################################
#Elementzugriff

a1 = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
print(a1)
print(a1[1]) # 1
print(a1[1:4]) # [1 2 3]
print(a1[-1]) #9
print(a1[6:]) # [6 7 8 9]

################################
# Mehrdimensionaler Elementzugriff

am = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Gesamte Matrix")
print(am)
print("Spalte 2")
print(am[:,1]) #Spalte 2
print("Zeile 2")
print(am[1,:]) #Zeile 2

#Auswahl einzelner Werte
print("Einzelne Werte")
print(am[[1,2],[0,1]]) #Positionen (1,0), (2,1)), also 4 und 8

# Auswahl über Bedingungen
ab = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
print("Bereich:" , ab)
print("ab < 5:")
print(ab[ab < 5])
print("~ab < 5:") #~ist 'not'
print(ab[~(ab < 5)])

# Umgang mit fehlenden Werten

a = np.array([np.nan, 1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])


for i in a:
    print(i)

########################################
# Manipulation von Array-Werten

am = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

am1 = am.reshape(6,2) # 6 Zeilen, 2 Spalten
print(am1)

am2 = am.flatten('C') #in 1-dim Array: Zeilenweise
print(am2)
print(am2)
am2 = am.flatten('F') #in 1-dim Array: Spaltenweise
print(am2)
am2 = am.ravel('C') # Macht das gleiche, erzeugt aber eine Kopie
am3 = am.flat[7] #Holt das 7.Element aus einem konstruierten 1-dim array
print(am3)

af = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

af1 = np.append(af,[[13,14,15,16]], axis=0) #Zeilenweise angehängt
print("append:")
print(af1)
af2 = np.split(af,2 , 1)
print("split:")
print(af2[0])
print(af2[1])

#Lösche die 3. Zeile in af
af3 = np.delete(af, 2,0);
print(af3)

#Schmeisse die doppelten hinaus und gib Ergebnis als 1-dim Array zurück
af4 = np.unique(af)
print(af4)

##########################################################################
# String - Funktionen

