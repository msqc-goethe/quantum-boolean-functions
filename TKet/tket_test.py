from pytket import *
import numpy as np
from pytket.circuit import Circuit, OpType
from pytket import qasm
from pytket.utils import Graph
from pytket.passes import auto_rebase, auto_rebase_pass, RebaseCustom, auto_squash_pass
from pytket.extensions.qiskit import AerBackend


from qiskit import *
from qiskit import Aer

backend = AerBackend()

#circ = qasm.circuit_from_qasm('unitary_qasm2.qasm')

#print(type(circ))

def main():
    with open('result_test2.txt', 'w') as f:
        f.write('#qubits cx p rx ry rz\n')
        for N in range(2, 25):
            circ = Circuit(N)
            circ.add_gate(OpType.CnX, range(N))
            #Graph(circ).save_DAG("before"+str(N))

            gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
            #gates2 = {OpType.Rx, OpType.Ry, OpType.Rz, OpType.PhasedX} 

            #gates = {OpType.PhasedX,OpType.Rz, OpType.Rx, OpType.Ry, OpType.CX}
            #custom = RebaseCustom(gates, cx_in_cy, tk1_to_rzry)
            #custom.apply(circ)
            custom = auto_rebase_pass(gates)
            #squash = auto_squash_pass(gates2)

            #print(circ.get_commads())
            #p = auto_rebase.auto_rebase_pass(gateset)
            #p.apply(circ)
            custom.apply(circ)
            #squash.apply(circ)
            #compiled_circuit = circ
            compiled_circuit = backend.get_compiled_circuit(circ)
            custom.apply(compiled_circuit)


            #print(compiled_circuit.get_unitary())
            #print(compiled_circuit.get_commands())
            #print("Number of qubits: " +str(N))
            f.write(str(N))
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

main()


#print(compiled_circuit.get_commands())

#Graph(compiled_circuit).save_DAG("test_unitary.png")