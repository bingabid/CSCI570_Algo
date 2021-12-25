import sys
import time
import os
from read_input import load_data, write_output
from alignment import get_alignment, get_alignment_efficient



if __name__=='__main__':

    # argument = sys.argv
    # input_txt =  argument[1]
    string1, string2 = load_data("input.txt")
    # print(string1)
    # print(string2)

    ''' Normal Dynamic Programming Solution'''
    start_time_dp = time.time()
    string1_alignment, string2_alignment, cost, memory = get_alignment(string1, string2)
    end_time_dp = time.time()
    total_time_dp = end_time_dp - start_time_dp
    # print(string1_alignment)
    # print(string2_alignment)
    # print(cost)
    # print(total_time_dp)
    # print(memory)
    write_output("output.txt", string1_alignment, string2_alignment, cost, total_time_dp, memory)
    

    # print(psutil.Process(os.getpid()).memory_info()[0] / 1024 ** 2)

    ''' Memory Efficient using Divide & Conquer with DP Solution'''
    start_time_dc = time.time()
    string1_alignment_me, string2_alignment_me, cost, memory = get_alignment_efficient(string1,string2)
    print(string1_alignment_me)
    print(string2_alignment_me)
    # mismatch_cost = {
    # 'AA':0, 'AC':110, 'AG':48, 'AT':94,
    # 'CA':110, 'CC':0, 'CG':118, 'CT':48,
    # 'GA':48, 'GC':118, 'GG':0, 'GT':110,
    # 'TA':94, 'TC':48, 'TG':110, 'TT':0
    # }
    # X_aligned, Y_aligned = string1_alignment_me, string2_alignment_me
    # cost = 0.0
    # for i in range(len(X_aligned)):
    #     if X_aligned[i] == '_' or Y_aligned[i] == '_':
    #         cost += 30.0
    #     else:
    #         cost += mismatch_cost[X_aligned[i] + Y_aligned[i]]
    print(cost)

    end_time_dc = time.time()
    total_time_dc = end_time_dc - start_time_dc
    print(total_time_dc)
    print(memory)
