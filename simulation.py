import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams.update({'font.size': 14})


sim_size = 10000
n = 2


def make_simulation(lambda_a = 2):

    lambda_c = 1000 * lambda_a
    lambda_d1 = 1.0459
    lambda_d2 = 1.8388

    def eval_va():
        return np.random.exponential(scale=1 / lambda_a)

    def eval_vc():
        return np.random.exponential(scale=1 / lambda_c)

    def eval_vd1():
        return np.random.exponential(scale=1 / lambda_d1)

    def eval_vd2():
        return np.random.exponential(scale=1 / lambda_d2)

    a = np.zeros((sim_size))
    c = np.zeros((sim_size))
    d = np.zeros((sim_size))

    for k in range(0, sim_size):

        V_a = eval_va()
        V_c = eval_vc()
        V_d1 = eval_vd1()
        V_d2 = eval_vd2()

        a[k] = max(V_a + a[k-1], c[k-n])
        c[k] = V_c + max(a[k], d[k-1])
        d[k] = V_d1 + V_d2 + c[k]

    W_q_each = c[1000:] - a[1000:]
    # W_q_each[W_q_each > 6] = 2
    # plt.boxplot(W_q_each)
    W_q = np.mean(W_q_each)
    print("Tempo médio de espera na fila: ", W_q)

    plt.show()

    return W_q_each


# if __name__ == '__main__':
#     """
#     Main method to make 10 executions of simulation for one lambda_a
#     """
#     W_q_list = list()
#     for _ in range(1):
#
#         W_q_list.append(make_simulation())
#
#     plt.boxplot(W_q_list)
#     plt.show()
#     print("Média: ", np.mean(W_q_list))

if __name__ == '__main__':
    """
    Main method to compare each lambda for one execution
    """
    W_q_list = list()
    lambda_a_list = [0.1, 0.4, 0.6, 1, 2]
    for la in lambda_a_list:

        W_q_list.append(make_simulation(lambda_a=la))

    plt.boxplot(W_q_list)
    plt.xticks(range(1, len(lambda_a_list)+1), lambda_a_list)
    plt.xlabel("$\lambda_a$")
    plt.ylabel("$w_q$")
    plt.show()