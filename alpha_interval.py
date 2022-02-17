import numpy as np


mean = 0.2113
var = 6.5e-5

mean = 1.0684
var = 4.1e-4

mean = 1.6658
var = 3.7e-4

mean = 2.3937
var = 6.0e-4

mean = 2.8754
var = 8.4e-4

t_student = 2.262
n = 10

aux = t_student * np.sqrt(var / n)

print(f"Intervalo: [{mean - aux}, {mean + aux}]")
