import numpy as np
from matplotlib import pyplot as plt

x = np.arange(100)
y = np.random.rand(100)

# plt.title("Matplotlib Zufallszahlen")
# plt.xlabel("Index")
# plt.ylabel("Zufallszahlen")
# plt.plot(x,y)
# plt.savefig("out/m1.png")
# plt.show()


# Details zum Plot-Aufruf
# Weitere Parameter unter: https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

# y2 = np.random.rand(100)
# plt.title("Matplotlib Zufallszahlen")
# plt.xlabel("Index")
# plt.ylabel("2 Zufallszahlen")
# plt.plot(x,y, "r-.")
# plt.plot(x,y2,"gd")
# plt.savefig("out/m2.png")
# plt.show()

###################################################
# Barplots
###################################################

# x = [5,8,10] # Position der Balken
# y = [12,16,6] # Höhe der Balken
#
# x2 = [6,9,11] # Werden für die grünen Balken verwendet
# y2 = [6,15,7]
# plt.bar(x, y, align = 'center')
# plt.bar(x2, y2, color = 'g', align = 'center')
# plt.bar(7, 5, color = 'r', align = 'center') #Geht auch ohne Array
# plt.title('Balkendiagramm')
# plt.xlabel('X - Achse')
# plt.ylabel('Y - Achse')
# plt.savefig("out/m3.png")
# plt.show()
#
#
# x = [1,2,3] # Position der Balken
# y = [12,16,6] # Höhe der Balken
#
# plt.bar(x,y, align = 'edge', width=0.4, bottom=10, color=['r','g','b'], tick_label=['rot','grün','blau'])
# plt.title('Balkendiagramm')
# plt.xlabel('X - Achse')
# plt.ylabel('Y - Achse')
# plt.savefig("out/m4.png")
# plt.show()

##########################################################
# Boxplot
##########################################################

# d = np.random.rand(100) * 100
# d = d.reshape(10,10)
#
# plt.boxplot(d, vert=True, # Horizontal oder Vertikal
# 	notch=False,  # Einbiegung beim Median
# 	patch_artist=True,  # Mit Farbe angefüllt
# 	labels=np.arange(10,20), # Beschriftung X-Achse
# 	boxprops=dict(facecolor='r', color='black'),  # Füllfarbe und Rahmenfarbe
# 	medianprops=dict(color='black')) # Farbe des Medianstrichs
#
# plt.savefig("out/m5.png")
# plt.show()


##########################################################
# Scatter-Plot
##########################################################

# x = np.random.rand(100) * 100
# y = np.random.rand(100)
# col = np.random.rand(100) * 100  # Diese Werte werden, wenn gewünscht, als Farben abgebildet
# size = np.random.rand(100) * 1000
# plt.scatter(x,y, # Die beiden Werte werden an den Achsen gegenübergestellt
#             c=col, # Farbwerte werden hier abgebildet
#             s=size, # Größe wird hier abgebildet
#             marker="*",
#             alpha=0.5) # Transparenz der Punkte
# plt.grid(True)
# plt.savefig("out/m6.png")
# plt.show()

##########################################################
# Histogram
##########################################################


x = np.random.normal(170, 10, 1000) #Normalverteilung (Mittelwert, Standardabweichung, Anzahl)
plt.hist(x, bins=20) #bins: Wie viele Balken
plt.savefig("out/m7.png")
plt.show()