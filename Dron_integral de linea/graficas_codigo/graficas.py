import numpy as np
import matplotlib.pyplot as plt
from graficar_curva import graficar

t_values = np.linspace(0, 5, 100)
t2_values = np.linspace(0.001, 1, 10)
t3_values = np.linspace(0.001, 5, 100)
t4_values = np.linspace(0.001, 1, 10)
graficar(t_values, t2_values, t3_values, t4_values)