import numpy as np

lambda_a = 1
lambda_c = 10 * lambda_a
lambda_d1 = 1
lambda_d2 = 1

variables = 9
equations = 10

A = np.zeros((variables, equations))

A[0, 0] = -lambda_a
A[0, 4] = lambda_d2

A[1, 0] = lambda_a
A[1, 1] = -(lambda_a + lambda_c)
A[1, 6] = lambda_d2


A[2, 1] = lambda_a
A[2, 2] = -lambda_c
A[2, 8] = lambda_d2

A[3, 1] = lambda_c
A[3, 3] = -(lambda_a + lambda_d1)

A[4, 3] = lambda_d1
A[4, 4] = -(lambda_a + lambda_d2)

A[5, 2] = lambda_c
A[5, 3] = lambda_a
A[5, 5] = -(lambda_a + lambda_d1)

A[6, 4] = lambda_a
A[6, 5] = lambda_d1
A[6, 6] = -(lambda_a + lambda_d2)

A[7, 5] = lambda_a
A[7, 7] = -lambda_d1

A[8, 6] = lambda_a
A[8, 7] = lambda_d1
A[8, 8] = lambda_d2

A[9, :] = 1