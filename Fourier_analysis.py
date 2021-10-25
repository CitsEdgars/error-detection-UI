import numpy as np
from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def get_harmonics_graph(binary, harmonics = 50, datapoints = 100):
    bit_count = len(binary)
    dx = 1/datapoints
    L = datapoints
    x = L * np.arange(0+dx, 1+dx, dx)
    n = len(x)
    n_bit = int(np.floor(n/bit_count))

    y = []
    for letter in binary:
        y.append(int(letter))

    f = np.zeros_like(x)
    for idx,val in enumerate(y):
        f[idx*n_bit:(idx+1)*n_bit] = y[idx]

    A0 = (np.sum(f) * dx * L) * 2/L
    fFS = A0/2
   
    A = np.zeros(harmonics)
    B = np.zeros(harmonics)
    for k in range(harmonics):
        A[k] = 2*np.sum(f * np.sin(2*np.pi * (k+1) * x/L)) * dx
        B[k] = 2*np.sum(f * np.cos(2*np.pi * (k+1) * x/L)) * dx
        fFS += A[k]*np.sin((k+1)*2*np.pi*x/L) + B[k]*np.cos((k+1)*2*np.pi*x/L)
        
    return fFS

def get_simple_graph(binary, datapoints = 100):
    bit_count = len(binary)

    dx = 1/datapoints
    L = datapoints
    x = L * np.arange(0+dx, 1+dx, dx)
    n = len(x)
    n_bit = int(np.floor(n/bit_count))

    y = []
    for letter in binary:
        y.append(int(letter))

    f = np.zeros_like(x)
    for idx,val in enumerate(y):
        f[idx*n_bit:(idx+1)*n_bit] = y[idx]
    
    return f
    