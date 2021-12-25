import random
import numpy as np
def random_dna_sequence(length):
    X = ''.join(random.choice('ACTG') for _ in range(length))
    Y = ''.join(random.choice('ACTG') for _ in range(length))
    return X, Y


if __name__=='__main__':
    X, Y = random_dna_sequence(16)
    print(X, Y)

    x_input = np.random.randint(1,3001,25)
    x_input = sorted(x_input)
    print(x_input)