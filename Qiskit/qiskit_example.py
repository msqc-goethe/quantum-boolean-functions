from qiskit import *
from qiskit.compiler import transpile
from qiskit.circuit.classicalfunction import BooleanExpression

op = BooleanExpression('a & b', name='AND')
circ = QuantumCircuit(3)
circ.append(op,range(3))
transpiled_circuit = transpile(circ, basis_gates=['rx', 'rz','ry' ,'p','cx'])


print(transpiled_circuit.count_ops())
transpiled_circuit.draw('mpl', filename='and_example')