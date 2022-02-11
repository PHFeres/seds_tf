import math

mu = 1.5
sigma = 1.1
N = 2

beta_2 = sigma**2 - (N - 2) * (mu**2 / N**2)
alpha = (2 * mu / N)

lambda_1 = 2 / (alpha + math.sqrt(2 * beta_2 - alpha**2))
lambda_2 = 2 / (alpha - math.sqrt(2 * beta_2 - alpha**2))

print(lambda_1, lambda_2)