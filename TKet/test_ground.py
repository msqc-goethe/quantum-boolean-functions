from pytket.circuit import Circuit, OpType
from pytket.passes import auto_rebase_pass
from pytket.extensions.qiskit import AerBackend
from pytket import Circuit
from pytket.circuit import ToffoliBox
from pytket.utils import Graph

permutation = {(0,1,0): (0,1,1) , (0,1,1): (0,1,0), (1,0,0): (1,0,1) , (1,0,1): (1,0,0)}
tb = ToffoliBox(n_qubits=3, permutation=permutation)

circ = Circuit(3)
circ.add_toffolibox(tb, range(3))

backend = AerBackend()
compiled_circuit = backend.get_compiled_circuit(circ)
Graph(compiled_circuit).save_DAG('tket_compiled_example_xor')

gates = {OpType.Rx, OpType.Ry, OpType.CX, OpType.Rz, OpType.PhasedX} 
rebase = auto_rebase_pass(gates)
rebase.apply(compiled_circuit)

Graph(compiled_circuit).save_DAG('tket_example_xor')