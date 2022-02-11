import numpy as np

lambda_a = 1
lambda_c = 10 * lambda_a
lambda_d1 = 1
lambda_d2 = 1

variables = 9
equations = 

A =
A = np.array([
    [-lambda_a,         0,                  0,              0,                  lambda_d2,                  0,      0,      0,      0],
    [lambda_a, -(lambda_a + lambda_c),      0,              0,                      0,                      0, lambda_d2,   0,      0],
    [   0,              lambda_a,       -lambda_c,          0,                      0,                      0,      0,      0,  lambda_d2],
    [   0,              lambda_c,           0,      -(lambda_a + lambda_d1),        0,                      0,      0,      0,      0],
    [   0,              0,                  0,              lambda_d1,      -(lambda_a + lambda_d2),        0,      0,      0,      0],
    []
])