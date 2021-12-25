import sys  
def load_data(input_txt):
    with open(input_txt) as f:
        input_text = f.read().splitlines()
        
    base_string1 = input_text[0]
    i=1
    base1 = []
    while input_text[i].isnumeric():
        base1.append(int(input_text[i]))
        i+=1
    base_string2 = input_text[i]
    # print(base_string1)
    # print(base1)
    base2 = []
    for j in range(i+1,len(input_text)):
        base2.append(int(input_text[j]))
    # print(base_string2)
    # print(base2)

    return generate_string(base_string1,base1,base_string2,base2)

def generate_string(base_string1, indices1, base_string2, indices2):
    string1, string2 = base_string1, base_string2
    for i in indices1:
        string1 = string1[:i+1] + string1 + string1[i+1:]

    for i in indices2:
        string2 = string2[:i+1] + string2 + string2[i+1:]

    return string1, string2

def write_output(output_txt, X, Y, cost, time, memory):
    with open(output_txt, 'w') as wf:
        x = X[:51] + " " + X[-50:] + '\n'
        y = Y[:51] + " " + Y[-50:] + '\n'
        wf.write(x)
        wf.write(y)
        wf.write(str(cost) + '\n')
        wf.write(str(time) + '\n')
        wf.write(str(memory))




if __name__ == "__main__":
    s1, s2 = load_data("input.txt")
    print(s1)
    print(sys.getsizeof(s1))
    print(s2)
    print(sys.getsizeof(s2))