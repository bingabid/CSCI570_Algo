import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from alignment import get_alignment
from dna_generator import random_dna_sequence

if __name__=='__main__':
    data_point = 25
    start_limit = 1
    end_limit = 3001
    y_time = []
    y_memory = []
    x_input = np.random.randint(start_limit, end_limit, data_point)
    # x_input = [int(x) for x in x_input]
    x_input = sorted(x_input)
    # for i in range(data_point):
    #     x_input.append(np.random.randint(limit))
    # x_input = sorted(x_input)

    for i in range(len(x_input)):
        X, Y = random_dna_sequence(x_input[i])
        # print(X, Y)
        start_time_dp = time.time()
        string1_alignment, string2_alignment, cost, memory = get_alignment(X, Y)
        end_time_dp = time.time()
        total_time_dp = end_time_dp - start_time_dp
        y_time.append(total_time_dp/1024)
        y_memory.append(memory)

    # plt.subplot(1, 2, 1)
    plt.plot(x_input, y_time, 'o:b', linestyle = 'dotted')
    plt.title("Time Complexity Analysis: dp")
    plt.xlabel("Input Size")
    plt.ylabel("Time(in sec)")
    plt.show()
    plt.savefig('basic_time.png')
    # plt.subplot(1, 2, 2)
    plt.plot(x_input, y_memory, 'o:r', linestyle = 'dotted')
    plt.title("Space Complexity Analysis: dp")
    plt.xlabel("Input Size")
    plt.ylabel("Memory (in KB)")
    plt.show()
    plt.savefig('basic_memory.png')