import numpy as np
from science_optimization.algorithms.linear_programming import Glop
from science_optimization.builder import OptimizationProblem
from science_optimization.problems import MIP
from science_optimization.solvers import Optimizer

lambda_a = 2
lambda_c = 1000 * lambda_a
lambda_d1 = 1.0459
lambda_d2 = 1.8388

n_variables = 9
n_equations = 10

A = np.zeros((n_equations, n_variables))

A[0, 0] = -lambda_a
A[0, 6] = lambda_d2

A[1, 0] = lambda_a
A[1, 7] = lambda_d2
A[1, 1] = -(lambda_a + lambda_c)

A[2, 1] = lambda_a
A[2, 8] = lambda_d2
A[2, 2] = -lambda_c

A[3, 1] = lambda_c
A[3, 3] = -(lambda_a + lambda_d1)

A[4, 2] = lambda_c
A[4, 3] = lambda_a
A[4, 4] = -(lambda_a + lambda_d1)

A[5, 4] = lambda_a
A[5, 5] = -lambda_d1

A[6, 3] = lambda_d1
A[6, 6] = -(lambda_a +lambda_d2)

A[7, 4] = lambda_d1
A[7, 6] = lambda_a
A[7, 7] = -(lambda_a + lambda_d2)

A[8, 7] = lambda_a
A[8, 5] = lambda_d1
A[8, 8] = -lambda_d2

A[9, :] = 1

b = np.zeros((n_equations, 1))
b[9, 0] = 1

c = np.zeros((n_variables, 1))

mipp = OptimizationProblem(builder=MIP(c=c, A=np.zeros((1, n_variables)), b=np.array([[0]]), Aeq=A, beq=b))

# builder optimization
mip_optimizer = Optimizer(opt_problem=mipp, algorithm=Glop())

results = mip_optimizer.optimize(debug=False)

results.info()

all_z = results.x

z_1 = all_z[0, 0]
z_2 = all_z[1, 0]
z_3 = all_z[2, 0]
z_4 = all_z[3, 0]
z_5 = all_z[4, 0]
z_6 = all_z[5, 0]
z_7 = all_z[6, 0]
z_8 = all_z[7, 0]
z_9 = all_z[8, 0]

theta = lambda_a * (z_1 + z_2 + z_4 + z_5 + z_7 + z_8)
L_q = (0 * (z_1 + z_4 + z_7) + 1 * (z_2 + z_5 + z_8) + 2 * (z_3 + z_6 + z_9))

W_q = L_q / theta

print("theta: ", theta)
print("L_q: ", L_q)
print("Tempo médio de espera na fila: ", W_q)

print()