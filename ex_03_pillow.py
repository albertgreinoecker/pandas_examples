from PIL import Image

# img = Image.open('img/htl-logo.png')
#
# print(img.format) # Speicherformat
# print(img.size) # Dimensionen
# print(img.mode) # Farbmodus
# img.show() # Anzeigen des Bildes im default-Bildeditor


#Laden des Bildes mit Matplotlib
#
# from matplotlib import image
# from matplotlib import pyplot
# image = image.imread('img/htl-logo.png')
# print(image.dtype) # Werte als float32 gespeichert
# print(image.shape) # (x,y, farbebenen) farb-ebenen = [r,g,b,opacity]
# print(image[0][0]) # Pixel links oben
# pyplot.imshow(image) # Bild auf die Zeichenfläche geben
# pyplot.show()


#Laden des Bildes als numpy-Array

from PIL import Image
from numpy import asarray
image = Image.open('img/htl-logo.png')
# Übertragen des Bildes in ein numpy-Array
data = asarray(image)
print(data[0][2]) #Pixel links oben
# Hier könnte die Manipulation stattfinden
print(data.shape) #Dimensionen des Bildes (x,y, farb-ebenen)
# So kann man aus dem numpy-array wieder ein PIL-Bild machen
image2 = Image.fromarray(data)

