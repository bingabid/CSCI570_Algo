import sys
import time
import os
from read_input import load_data, write_output
from alignment import get_alignment, get_alignment_efficient



if __name__=='__main__':

    argument = sys.argv
    input_txt =  argument[1]
    output_txt = "output.txt"
    string1, string2 = load_data(input_txt)
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
    write_output(output_txt, string1_alignment, string2_alignment, cost, total_time_dp, memory)