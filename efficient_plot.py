import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from alignment import get_alignment_efficient
from dna_generator import random_dna_sequence

if __name__=='__main__':
    data_point = 10
    start_limit = 1
    end_limit = 50000
    y_time = []
    y_memory = []
    x_input = np.random.randint(start_limit, end_limit, data_point)
    x_input = sorted(x_input)

    for i in range(len(x_input)):
        X, Y = random_dna_sequence(x_input[i])
        # print(X, Y)
        start_time_dp = time.time()
        string1_alignment, string2_alignment, cost, memory = get_alignment_efficient(X, Y)
        end_time_dp = time.time()
        total_time_dp = end_time_dp - start_time_dp
        y_time.append(total_time_dp/1024)
        y_memory.append(memory)

    plt.plot(x_input, y_time,'o:b', linestyle = 'dotted')
    plt.title("Time Complexity Analysis: dp & dc")
    plt.xlabel("Input Size(n)")
    plt.ylabel("Time(in sec)")
    plt.show()
    plt.plot(x_input, y_memory,'o:r', linestyle = 'dotted')
    plt.title("Space Complexity Analysis: dp & dc")
    plt.xlabel("Input Size(n)")
    plt.ylabel("Memory (in KB)")
    plt.show()