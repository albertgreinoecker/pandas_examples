from PIL import Image
from numpy import asarray
import numpy as np
from matplotlib import pyplot as plt

image = Image.open('img/htl-logo.png')

data = asarray(image)
print(data.shape)

print(data[0,0]) # Pixel an den bestimmten Stellen
print(data[0][0][0])
print(data[100,100])
print(data[100,100,0])
#d = data[...],[...],[0]  #Alle rot-Werte
#data[:,:,0] = 255 # Setze alle rot-Werte auf 100
print(data[100][100][0])
#data[...][...] = [255.0,255,255,1]
#print(d)

print(data[100,100,0:3]) # Alle Farbwerte

print(data[:,100,0])

print("grün")
print(data[data[:,:,1] < 100])  # Alle Grün-Werte kleiner 100

print("Zuweisung")
data[:,:,0] = 100 # Alle rot-Werte auf 100 setzen
#lt_100 = np.where(data[:,:,1] < 100)
#data[lt_100] = 100


red = np.ravel(data[:,:,0 ]) #Alle rot-Werte
mean = np.mean(red)
print(mean)
print(red)
plt.boxplot(red)
plt.show()
print( np.where(data[:,:,1] < 100))
Image.fromarray(data).save('img/htl-logo-numpy.png')