#inspired by: https://klyshko.github.io/teaching/2019-02-22-teaching
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('audio/Applaus.wav')  #freq, sound
print(data.shape)

#data = data / 2.0**15

plt.subplot(2,1,1)
plt.plot(data[:,0], 'r')
plt.xlabel("left channel, sample #")
plt.subplot(2,1,2)
plt.plot(data[:,1], 'b')
plt.xlabel("right channel, sample #")
plt.tight_layout()
plt.savefig("out/s1_over_time.png")

#plt.plot(data[:,0])
plt.show()

#fft_out = fft(data) # np.fft.rfft
#fft_out_parts = fft_out

fft_spectrum = np.fft.rfft(data)
freq = np.fft.rfftfreq(data.size, d=1./rate)
freq = np.delete(freq, -1)

#print(fft_out_parts.shape )
#plt.plot(fft_out)
#plt.plot(data, np.abs(fft_out))
print(freq)
plt.plot(freq, np.abs(fft_spectrum[:,0]))
#print(fft_out.shape)
plt.savefig("out/s2_frequencies.png")

plt.plot(freq[500:3000], np.abs(fft_spectrum[500:3000,0]))
#print(fft_out.shape)
plt.savefig("out/s2_frequencies_part.png")