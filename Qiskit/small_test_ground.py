import numpy as np
from qiskit import *
from qiskit.visualization import plot_state_city,plot_histogram
from qiskit.quantum_info.operators import Operator
from qiskit.compiler import transpile
from qiskit.providers.ibmq import least_busy
from qiskit.circuit.classicalfunction import BooleanExpression
from qiskit.transpiler.coupling import CouplingMap
import qiskit.quantum_info as qi

import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)


def create_circuit_new():
        from qiskit import Aer

        #Changing the simulator 
        backend = Aer.get_backend('unitary_simulator')


        i = 3
        c_out = BooleanExpression('(c & (a ^ b)) | (a & b)', name='c_out')
        s = BooleanExpression('a ^ b ^ c', name='S')

        circ = QuantumCircuit(i+2)
        circ.append(c_out,range(i+1))
        circ.append(s, [0,1,2,4])

        circ.draw('mpl', filename='full_adder')
        transpiled_circuit = transpile(circ.reverse_bits(), basis_gates=['rx', 'rz','ry' ,'p','cx'])

        #transpiled_circuit.draw('mpl', filename='and_custome'+str(i))

        #job execution and getting the result as an object
        job = execute(transpiled_circuit, backend)
        result = job.result()

        #get the unitary matrix from the result object
        #with open('fulladdrm.txt', 'w') as f:
                #f.write(str(result.get_unitary(transpiled_circuit, decimals=3)))

        pprint_operator(result.get_unitary(transpiled_circuit, decimals=3))

        
        print("Gates used: "+ str(transpiled_circuit.count_ops()) + "\n")


def pprint_operator(op):
    for line in op.data:
        for e in line:
            if e == 1:
                print('\033[38;2;0;0;0;48;2;0;255;0m1', end=' ')
            else:
                print('\033[38;2;0;0;0;48;2;255;0;255m0', end=' ')
        print('\n', end='')


create_circuit_new()