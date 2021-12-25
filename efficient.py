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

    start_time_dc = time.time()
    string1_alignment_me, string2_alignment_me, cost, memory = get_alignment_efficient(string1,string2)
    end_time_dc = time.time()
    total_time_dc = end_time_dc - start_time_dc

    # print(string1_alignment_me)
    # print(string2_alignment_me)
    # print(cost)
    # print(total_time_dc)
    # print(memory)
    write_output(output_txt, string1_alignment_me, string2_alignment_me, cost, total_time_dc, memory)