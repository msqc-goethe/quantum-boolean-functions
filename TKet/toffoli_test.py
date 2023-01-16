from pytket import *
import numpy as np
from pytket.circuit import Circuit, OpType
from pytket.passes import auto_rebase_pass
from pytket.extensions.qiskit import AerBackend
from pytket import Circuit
from pytket.circuit import ToffoliBox

from pytket.architecture import Architecture
from pytket.circuit import Node
from pytket.mapping import MappingManager

from pytket.mapping import LexiLabellingMethod, LexiRouteRoutingMethod
from pytket.utils import Graph

from pytket.architecture import SquareGrid

from pytket.architecture import RingArch

from itertools import product
backend = AerBackend()



def to_next_power(i):
    l = [4,9,16,25]
    for k in l:
        if i < k:
            return k

def xor_mask(N):
    mask = []
    tuples = list(product([0,1],repeat=N))
    for i in tuples:
        s = 0
        for k in i:
            if k == 1:
                s = s+1
        if s % 2 == 1:
            mask.append(1)
        else:
            mask.append(0)
    return mask

def create_xor_permutation(N):
    #first create mask
    mask = xor_mask(N-1)
    tuples= list(product([0,1], repeat=N))
    tuples_fixed = list(product([0,1], repeat=N))

    permutation = {}
    for k in range(2,len(tuples_fixed))[::2]:
        if mask[int(k/2)] == 1:
            temp = tuples[k]
            tuples[k] = tuples[k+1]
            tuples[k+1] = temp
    
    for i in range(len(tuples_fixed)):
        permutation.update({tuples_fixed[i]:tuples[i]})

    return permutation

def create_and_permutation(N):
    permutation = {}
    tuples= list(product([0,1], repeat=N))
    tuples_fixed = list(product([0,1], repeat=N))
    temp = tuples[-1]
    tuples[-1] = tuples[-2]
    tuples[-2] = temp

    for i in range(len(tuples_fixed)):
        permutation.update({tuples_fixed[i]:tuples[i]})

    return permutation

def create_or_permutation(N):
    permutation ={}
    tuples = list(product([0,1],repeat=N))
    tuples_fixed = list(product([0,1],repeat=N))

    for k in range(2,len(tuples_fixed))[::2]:
        #print(k)
        temp = tuples[k]
        tuples[k] = tuples[k+1]
        tuples[k+1] = temp
    
    for i in range(len(tuples_fixed)):
        permutation.update({tuples_fixed[i]:tuples[i]})

    
    #print(tuples_fixed)
    #print(tuples)

    return permutation

def main():

    N = 7
    with open('toffoli_test_tk1_xor.txt', 'w') as f:
        #f.write('#qubits cx p rx ry rz\n')
        f.write('#qubits cx tk1\n')
        for i in range(3,N):
            gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
            custom = auto_rebase_pass(gates)

            permutation = create_xor_permutation(i)
            print('Create Permutation Worked')
            # Construct a two qubit ToffoliBox to perform the permutation
            tb = ToffoliBox(n_qubits=i, permutation=permutation)
            print('Create Toffoli Gate worked')
            circ = Circuit(i)
            circ.add_toffolibox(tb, range(i)) # Add the ToffoliBox defined above to our circuit

            compiled_circuit = backend.get_compiled_circuit(circ)
            print('Get Compiled Circuit Worked')
            #custom.apply(compiled_circuit)
            #print('apply custome worked')

            #print(compiled_circuit.get_commands())          # Display circuit commands

            #print("Statevector: " + str(circ.get_statevector()))
            print(i)
            f.write(str(i))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.CX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.TK1)))
            """f.write(str(compiled_circuit.n_gates_of_type(OpType.PhasedX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rx)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Ry)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rz)))"""

            f.write("\n")
    return


def small_circuit():
    N = 9
    with open('two_of_three.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
        custom = auto_rebase_pass(gates)

        permutation = {(0,1,1,0):(0,1,1,1), (0,1,1,1):(0,1,1,0), (1,0,1,0):(1,0,1,1), (1,0,1,1):(1,0,1,0), (1,1,0,0):(1,1,0,1) , (1,1,0,1):(1,1,0,0), (1,1,1,0):(1,1,1,1), (1,1,1,1):(1,1,1,0)}
        # Construct a two qubit ToffoliBox to perform the permutation
        tb = ToffoliBox(n_qubits=4, permutation=permutation)
        circ = Circuit(4)
        circ.add_toffolibox(tb, range(4)) # Add the ToffoliBox defined above to our circuit

        compiled_circuit = backend.get_compiled_circuit(circ)
        custom.apply(compiled_circuit)

        f.write(str(4))
        f.write(' ')
        f.write(str(compiled_circuit.n_gates_of_type(OpType.CX)))
        f.write(' ')
        f.write(str(compiled_circuit.n_gates_of_type(OpType.PhasedX)))
        f.write(' ')
        f.write(str(compiled_circuit.n_gates_of_type(OpType.Rx)))
        f.write(' ')
        f.write(str(compiled_circuit.n_gates_of_type(OpType.Ry)))
        f.write(' ')
        f.write(str(compiled_circuit.n_gates_of_type(OpType.Rz)))
        f.write("\n")
    return

def architecture_test():
    n = [Node("n", i) for i in range(3)]
    #arc = Architecture([[n[0], n[1]], [n[1], n[2]]])
    arc = RingArch(3)


    gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
    custom = auto_rebase_pass(gates)

    circ = Circuit(3)
    permutation = create_and_permutation(3)

    tb = ToffoliBox(n_qubits=3, permutation=permutation)
    circ.add_toffolibox(tb, [2,1,0])

    mapping_manager = MappingManager(arc)
    lexi_label = LexiLabellingMethod()
    lexi_route = LexiRouteRoutingMethod(10)


    compiled_circuit = backend.get_compiled_circuit(circ)
    mapping_manager.route_circuit(compiled_circuit,[lexi_label,lexi_route])
    Graph(compiled_circuit).save_DAG("mapping_manager_ring_test")
    #mapper = DecomposeMultiQubitsCX()
    #cu = CompilationUnit(circ)
    #mapper.apply(cu)
    #circ1 = cu.circuit

    custom.apply(compiled_circuit)

    #print('Get Compiled Circuit Worked')
    #custom.apply(compiled_circuit)

    print(compiled_circuit.n_gates_of_type(OpType.CX))
    print('apply custome worked')

    return

def pytket_architecture_toffolibox():
    N = 7
    with open('ring_architecture_xor.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for i in range(3,N):
            #create circuit
            circ = Circuit(i)
            permutation = create_xor_permutation(i)
            tb = ToffoliBox(n_qubits=i, permutation=permutation)
            circ.add_toffolibox(tb, list(reversed(range(i))))

            #create layout
            arc = RingArch(i)
            mapping_manager = MappingManager(arc)
            lexi_label = LexiLabellingMethod()
            lexi_route = LexiRouteRoutingMethod(10)

            #define gate set
            gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
            custom = auto_rebase_pass(gates)

            #compile circuit
            compiled_circuit = backend.get_compiled_circuit(circ)
            mapping_manager.route_circuit(compiled_circuit,[lexi_label,lexi_route])

            custom.apply(compiled_circuit)

            f.write(str(i))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.CX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.PhasedX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rx)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Ry)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rz)))
            f.write("\n")
    return

def pytket_architecture_toffolibox_grid():
    N = 7
    with open('grid_architecture_or.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for i in range(3,N):
            #define gates
            gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
            custom = auto_rebase_pass(gates)

            circ = Circuit(i)
            permutation = create_or_permutation(i)

            tb = ToffoliBox(n_qubits=i, permutation=permutation)

            circ.add_toffolibox(tb, list(reversed(range(i))))
            
            square = int(np.sqrt(to_next_power(i)))
            arc = SquareGrid(square,square)
            mapping_manager = MappingManager(arc)
            lexi_label = LexiLabellingMethod()
            lexi_route = LexiRouteRoutingMethod(10)


            compiled_circuit = backend.get_compiled_circuit(circ)
            mapping_manager.route_circuit(compiled_circuit,[lexi_label,lexi_route])

            custom.apply(compiled_circuit)

            print('Good Work: ' + str(i))
            #print("Statevector: " + str(circ.get_statevector()))
            f.write(str(i))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.CX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.PhasedX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rx)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Ry)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rz)))
            f.write("\n")
    return

def pytket_architecture_toffolibox_line():
    N = 7
    with open('line_architecture_xor.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for i in range(3,N):
            #define gates
            gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
            custom = auto_rebase_pass(gates)

            circ = Circuit(i)
            permutation = create_xor_permutation(i)

            tb = ToffoliBox(n_qubits=i, permutation=permutation)

            circ.add_toffolibox(tb, list(reversed(range(i))))

            n = [Node("n", j) for j in range(i)]
            couple = []
            for j in range(len(n)-1):
                couple.append([n[j],n[j+1]])
            print(couple)
            arc = Architecture(couple)
            mapping_manager = MappingManager(arc)
            lexi_label = LexiLabellingMethod()
            lexi_route = LexiRouteRoutingMethod(10)


            compiled_circuit = backend.get_compiled_circuit(circ)
            mapping_manager.route_circuit(compiled_circuit,[lexi_label,lexi_route])

            custom.apply(compiled_circuit)

            #print('Get Compiled Circuit Worked')
            #custom.apply(compiled_circuit)
            print('Good Work: ' + str(i))
            #print("Statevector: " + str(circ.get_statevector()))
            f.write(str(i))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.CX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.PhasedX)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rx)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Ry)))
            f.write(' ')
            f.write(str(compiled_circuit.n_gates_of_type(OpType.Rz)))
            f.write("\n")
    return
#create_and_permutation(3)
main()
#small_circuit()
#architecture_test()
#pytket_architecture_toffolibox_grid()
#pytket_architecture_toffolibox_line()

#create_or_permutation(3)
#print(create_xor_permutation(3))