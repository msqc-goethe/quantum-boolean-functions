import numpy as np
from qiskit import *
from qiskit.compiler import transpile
from qiskit.circuit.classicalfunction import BooleanExpression
from qiskit.transpiler.coupling import CouplingMap

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

op_dict = {
    'cx' : 0,
    'p' : 0,
    'rx' : 0,
    'ry' : 0,
    'rz': 0
}


def two_of_three():
    return BooleanExpression('(a&b) | (b&c)| (a&c)')

def always_zero():
    return BooleanExpression('a & ~a', name='always zero')

def always_one():
    return BooleanExpression('a | ~a | b | c', name='always one')

def id():
    return BooleanExpression('a', name='id')

def create_bool_list(n):
    l = []
    for i in range(2**n):
        l.append(1)
    l[0] = 0
    print(l)
    return l


#XOR Representation
def create_bool_expr_xor(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '^'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='XOR')
    return expr

#AND Representation
def create_bool_expr_AND(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '&'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='AND')
    return expr

def create_bool_expr_mixed(n):
    expr_string = ''
    for i in range(n):
        if i%2==0:
            expr_string += abc[i] + '&'
        else:
            expr_string += abc[i] + '|'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='MIXED')
    return expr
    

#OR Representation
def create_bool_expr_OR(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '|'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='OR')
    return expr

def create_id_matrix(n):
    matrix = []
    matrix = np.identity(2**(n+1))
    return matrix

def to_next_power(i):
    l = [4,9,16,25]
    for k in l:
        if i < k:
            return k

def start_qiskit_workflow():
    with open('qiskit_and_ring_example.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for i in range(2, 11):
            op = create_bool_expr_AND(i)
            circ = QuantumCircuit(i+1)
            circ.append(op,range(i+1))

            #couple = CouplingMap().from_line(i+1)
            
            couple = CouplingMap().from_ring(i+1)
            
            #square = int(np.sqrt(to_next_power(i+1)))
            #couple = CouplingMap().from_grid(num_columns=square, num_rows=square)

            transpiled_circuit = transpile(circ, basis_gates=['rx', 'rz','ry' ,'p','cx'],optimization_level=3, coupling_map=couple)

            f.write(str(i+1) + " ")
            for k,v in transpiled_circuit.count_ops().items():
                op_dict.update({str(k) : v})

            f.write(str(op_dict['cx']) + " ")
            f.write(str(op_dict['p']) + " ")
            f.write(str(op_dict['rx']) + " ")
            f.write(str(op_dict['ry']) + " ")
            f.write(str(op_dict['rz']))
            f.write("\n")

start_qiskit_workflow()

