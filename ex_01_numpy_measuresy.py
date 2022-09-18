import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

a1 = np.random.normal(170,10, 1000); # Array zur Veranschaulichung der Berechnungen
print(np.sort(a1))
plt.hist(np.sort(a1), bins=30)
#plt.plot(np.sort(a1))
plt.show()
#print (a1)
print("LAGEMAßE:")
print("Mittelwert", a1.mean())
print("Median", np.median(a1))

print("10% - Quantil", np.quantile(a1,0.1))
print("unteres Quartil", np.quantile(a1,0.25))
print("Median", np.quantile(a1,0.5))
print("Minimum", np.min(a1))
print("Maximum", np.max(a1))

a2 = np.random.randint(10,20,500)
m = stats.mode(a2)
print("Modus", m.mode[0], m.count[0])

print("STREUUNGSMAßE")
print("Standardabweichung", np.std(a1))
print("Mittleren 95%", np.mean(a1) - np.std(a1)*2, np.mean(a1)  + np.std(a1)*2)
print("Spannweite:", a1.max() - a1.min())
