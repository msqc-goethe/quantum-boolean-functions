from os import listdir
import glob
op_list = {
    'CZ': 0,
    'RX': 0,
    'RZ': 0,
    'XY': 0,
}

reset = {
    'CZ': 0,
    'RX': 0,
    'RZ': 0,
    'XY': 0,
}


def main():
    data = []
    lines = []
    #print(listdir('Ring/AND'))
    for file in glob.glob('*.txt'):

        with open(file) as f:
            lines = f.readlines()
        lines = lines[:-1]
        lines = lines[2:]

        for line in lines:
            v = op_list[str(line[:2])]
            v = v +1
            op_list.update({str(line[:2]):v})
        
        print(file)
        print(op_list)
        data.append(op_list)

        for k in op_list:
            op_list[k] = 0
        
    #write_data_to_file(data)

def one_file():
    data = []
    lines = []
    with open('qasm_pyquil_always_two_of_three.txt') as f:
            lines = f.readlines()
    lines = lines[:-1]
    lines = lines[2:]

    for line in lines:
            v = op_list[str(line[:2])]
            v = v +1
            op_list.update({str(line[:2]):v})
        
    print(op_list)
    data.append(op_list)

    for k in op_list:
        op_list[k] = 0


one_file()  
#main()

