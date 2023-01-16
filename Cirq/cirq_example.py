import cirq
import numpy as np

AND_GATE = [[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0]]

qubits = cirq.LineQubit.range(3)
and_gate = cirq.MatrixGate(np.array(AND_GATE))
circuit = cirq.Circuit()
        
circuit.append(and_gate(qubits[0], qubits[1], qubits[2]))

final = cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset())
