from qiskit import *
from qiskit import IBMQ

from pytket import Circuit
from pytket.utils import Graph
from pytket.extensions.qiskit import IBMQBackend, AerStateBackend

#IBMQ.save_account('7d24ce1ef47e687f39c2885a8af0ca36021c60ac2607fe2680c5bb10a167e3a789fa8d0231e8bd566bc0f9c81d8245558392c8026d3cc1c1fb585fa17d5aa71d')
IBMQ.load_account()

from pytket import Circuit
from pytket.extensions.qiskit import AerBackend

circ = Circuit(3)
circ.CCX(0,1,2).measure_all()

backend = AerBackend()
if not backend.valid_circuit(circ):
    compiled_circ = backend.get_compiled_circuit(circ)
    assert backend.valid_circuit(compiled_circ)

    print(compiled_circ.get_commands())

    Graph(compiled_circ).save_DAG("AND_SIM")

