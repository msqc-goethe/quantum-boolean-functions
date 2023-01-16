import cirq
import numpy as np
import sympy

def pprint_operator(op):
    for line in op:
        for e in line:
            print(int(e+0.9), end=' ')
        print('\n', end='')

qubits = cirq.LineQubit.range(6)
#bg = cirq.BooleanHamiltonianGate(['x0', 'x1'],['x0 ^ x1'],0.25).on(*qubits)
circuit = cirq.BooleanHamiltonianGate(parameter_names=['x0', 'x1', 'x2'], boolean_strs=['x0 & x1 & x2'], theta=-3.581264067285007)
#print([f"x{i}" for i in range(len(qubits))])
pprint_operator(cirq.unitary(circuit))

#circuit = cirq.Circuit()
#circuit = cirq.Circuit(cirq.X(qubit) ** 0.5, cirq.measure(qubit, key='m'))
#qubits[1],qubits[2], qubits[3]
#circuit.append(bg)

#final = cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset())
#print(final)


