import numpy as np
import matplotlib.pyplot as plt

tmax = 1
dt = 0.0025
t = np.arange(0, tmax, dt)

freq = float(input())
wave = np.sin(freq * np.cos(2 * np.pi * t))

signal = np.fft.fft(wave, t.size)

freqs = np.fft.fftfreq(t.size, dt)

Spectrum = np.abs(signal) / t.size
L = np.arange(1, t.size // 2, dtype=int)

print(freqs[L][Spectrum[L].argmax()])