from bqskit import Circuit, compile
from bqskit.qis import UnitaryMatrix
from bqskit.qis.permutation import PermutationMatrix
from bqskit.ir import Gate, Operation
from bqskit.ir.gates import CXGate,RXGate,RYGate,RZGate,PhasedXZGate
from bqskit import MachineModel
from bqskit.compiler import Compiler
from bqskit.passes import LEAPSynthesisPass
from bqskit.exec import CircuitRunner

import numpy as np


def create_id(n):
    return np.identity(n*2)

def simple_construct_rev_operation(lookup_table):
    m = create_id(len(lookup_table))
    for i, b in enumerate(lookup_table):
        if b == 1:
            #m.swap_rows(i*2, i*2+1)
            m[[i*2,i*2+1]] = m[[i*2+1,i*2]]
    return m

def define_gate(n):
    l = []
    for i in range(2**n):
        l.append(0)
    l[2**n -1] = 1
    print(l)
    return l


def main():

    op = UnitaryMatrix(simple_construct_rev_operation(define_gate(3)))
    #p = PermutationMatrix(op)
    gs= {CXGate(),RZGate(),RYGate(),RXGate(),PhasedXZGate()}
    model = MachineModel(num_qudits=5,gate_set=gs)
    circ = Circuit.from_unitary(op)
    #l =LEAPSynthesisPass()

    #p = simple_construct_rev_operation(define_gate(2))

    #print(l.run(circ))
    print(circ)

    toffoli_circuit = compile(circ,optimization_level=1,max_synthesis_size=4)
    print(toffoli_circuit.gate_counts)
    return




def test():
    gs= {CXGate(),RZGate(),RYGate(),RXGate(),PhasedXZGate()}
    model = MachineModel(num_qudits=3,gate_set=gs)


    circ = Circuit.from_file('2hope.qasm')
    comp = compile(circ, model=model)
    print(comp.get_unitary())
    print(comp.gate_counts)

    return

test()
