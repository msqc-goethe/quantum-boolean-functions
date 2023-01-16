import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_state_city,plot_histogram
from qiskit.quantum_info.operators import Operator
from qiskit.compiler import transpile
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller
from qiskit.providers import ibmq
from qiskit.providers.ibmq import least_busy
from qiskit.circuit.classicalfunction import BooleanExpression
from qiskit.transpiler.coupling import CouplingMap
import qiskit.quantum_info as qi

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
def create_expr_xor(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '^'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='XOR')
    return expr

#AND Representation
def create_bool_expr(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '&'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='AND')
    #print(expr.definition)
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
    print(expr.definition)
    return expr
    

#OR Representation
def create_bool_expr_OR(n):
    expr_string = ''
    for i in range(n):
        expr_string += abc[i] + '|'
    expr_string = expr_string[:-1]

    expr = BooleanExpression(expr_string, name='OR')
    print(expr.definition)
    return expr

def create_id_matrix(n):
    matrix = []
    matrix = np.identity(2**(n+1))
    return matrix

def create_unitary_expr(n):
    e = 2**(n+1)
    matrix = create_id_matrix(n)

    #Swap last two rows
    matrix[e-2][e-1] = 1
    matrix[e-2][e-2] = 0
    matrix[e-1][e-2] = 1
    matrix[e-1][e-1] = 0
    print(matrix)
    return matrix

def to_next_power(i):
    l = [4,9,16,25]
    for k in l:
        if i < k:
            return k


def create_circuit_new():
    with open('OR_circ_test.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for i in range(2,7):
            op = create_bool_expr_OR(i)
            print(i)
            circ = QuantumCircuit(i+1)
            circ.append(op,range(i+1))

            #couple = CouplingMap().from_line(i+1)
            couple = CouplingMap().from_ring(i+1)
            #square = int(np.sqrt(to_next_power(i+1)))
            #couple = CouplingMap().from_grid(num_columns=square, num_rows=square)
            #print(couple)

            #circ.qasm(filename='qasmfile' +str(i)+'.qasm')
            #transpiled_circuit = transpile(circ, backend=backend_sim, basis_gates=['id', 'rz', 'sx', 'x', 'cx', 'reset'], coupling_map=CouplingMap([[0,1],[1,0],[1,2],[2,1],[1,3],[3,1],[3,4],[4,3]], "test"))
            #transpiled_circuit.draw('mpl', filename='and_bool_expr_quito_OR'+str(i))
            #transpiled_circuit = transpile(circ, basis_gates=['rx', 'rz','ry' ,'p','cx'],optimization_level=3, coupling_map=couple)

            transpiled_circuit = transpile(circ, basis_gates=['rx', 'rz','ry' ,'p','cx'],optimization_level=3, coupling_map=couple)
            #if i <= 5 : transpiled_circuit.draw('mpl', filename='and_ring'+str(i))
            #transpiled_circuit.qasm(filename=str(i)+'hope.qasm')

            #print(transpiled_circuit.count_ops())
            
            #f.write("Instruction used: " + str(op) + "\n")
            #f.write(str(op.definition) + '\n')
            #f.write(str(qi.Operator(transpiled_circuit).data))



            #f.write('#qubits:' + str(i+1)+' ')
            f.write(str(i+1) + " ")
            for key,value in transpiled_circuit.count_ops().items():
                #f.write(str(key) + ":" + str(value)+ " ")
                op_dict.update({str(key) : value})

            f.write(str(op_dict['cx']) + " ")
            f.write(str(op_dict['p']) + " ")
            f.write(str(op_dict['rx']) + " ")
            f.write(str(op_dict['ry']) + " ")
            f.write(str(op_dict['rz']))
            f.write("\n")
           
def small_circuits():
    with open('qiskit_id', 'w') as f:
        #op = two_of_three()
        #op = always_zero()
        #op = always_one()
        op = id()

        circ = QuantumCircuit(2)
        circ.append(op,range(2))

        couple = CouplingMap().from_line(2)
        #couple = CouplingMap().from_ring(4)
        #square = int(np.sqrt(to_next_power(i+1)))
        #couple = CouplingMap().from_grid(num_columns=square, num_rows=square)
        #print(couple)

        transpiled_circuit = transpile(circ, basis_gates=['rx', 'rz','ry' ,'p','cx'],optimization_level=3)
        transpiled_circuit.draw('mpl', filename='id')

        print(transpiled_circuit.count_ops())

        f.write('#qubits:' + str(2)+' ')
        for key,value in transpiled_circuit.count_ops().items():
            f.write(str(key) + ":" + str(value)+ " ")
        f.write("\n")


#create_circuit(backend_sim)
create_circuit_new()

#small_circuits()

