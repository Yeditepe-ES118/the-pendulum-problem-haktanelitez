import numpy as np

def find_period(L0, L1):
    
    g = 9.81
    
    T0 = 2 * np.pi * np.sqrt(L0 / g)
    T1 = 2 * np.pi * np.sqrt(L1 / g)

    print(f"When L =  {float(L0)} m, T = {T0:.1f} s")
    
    for L in range(L0 + 1, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        
        print(f"When L = {float(L)} m, T = {T:.1f} s")
            
    return T0, T1