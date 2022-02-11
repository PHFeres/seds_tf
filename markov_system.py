import numpy as np
from science_optimization.algorithms.linear_programming import Glop
from science_optimization.builder import OptimizationProblem
from science_optimization.problems import MIP
from science_optimization.solvers import Optimizer

lambda_a = 0.1
lambda_c = 1000 * lambda_a
lambda_d1 = 1.0459
lambda_d2 = 1.8388

n_variables = 9
n_equations = 10

A = np.zeros((n_equations, n_variables))

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

print("aquii", sum(results.x))