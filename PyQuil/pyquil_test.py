from pyquil import get_qc, Program
from pyquil.gates import H, CNOT, MEASURE
from pyquil.quilbase import Declare
import numpy as np
from pyquil.api import QVMCompiler
from itertools import product
from pyquil.quilbase import DefPermutationGate

from pyquil.quantum_processor.transformers.graph_to_compiler_isa import graph_to_compiler_isa
import networkx as nx
import matplotlib.pyplot as plt
from pyquil.quantum_processor import NxQuantumProcessor
from pyquil.api._quantum_computer import _get_qvm_with_topology


annddd = [0,0,0,0,0,0,0,1]

def define_gate_xor(N):
    N = N-1
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



def define_gate(n):
    l = []
    for i in range(2**n):
        l.append(0)
    l[2**n -1] = 1
    print(l)
    return l

def define_gate_or(n):
    l = []
    for i in range(2**n):
        l.append(1)
    l[0] = 0
    print(l)
    return l

def create_id(n):
    return np.identity(n*2)

def create_id_pow(i):
    return np.identity(2**i)


def simple_construct_rev_operation(lookup_table):
    m = create_id(len(lookup_table))
    for i, b in enumerate(lookup_table):
        if b == 1:
            #m.swap_rows(i*2, i*2+1)
            m[[i*2,i*2+1]] = m[[i*2+1,i*2]]
    return m


def main2():
    qc = get_qc("9q-square-qvm", compiler_timeout=600)
    for i in range(3,10):
        #op = simple_construct_rev_operation(create_id(i))
        op = create_id_pow(i)

        p = Program().defgate("op", op)
        l = range(i)
        opl = ['op']
        b = [*opl,*l]
        t = tuple(b)
        p.inst(t)

        #print(qc.compile(p))
        with open(str(i)+'qasm_id_square.txt', 'w') as f:
            f.write(str(qc.compile(p)))

def small_circuits():
    qc = get_qc("2q-qvm", compiler_timeout=600)
    #op = simple_construct_rev_operation(create_id(i))
    op = simple_construct_rev_operation([0,1])

    p = Program().defgate("op", op)
    l = range(2)
    opl = ['op']
    b = [*opl,*l]
    t = tuple(b)
    p.inst(t)

    #print(qc.compile(p))
    with open('qasm_pyquil_id.txt', 'w') as f:
        f.write(str(qc.compile(p)))



def permutation_test():
    
    qc = get_qc("3q-qvm", compiler_timeout=600)
    cnx = DefPermutationGate('CNX', [0,2,3,5,7,1,4,6])

    op = cnx.get_constructor()
    circ = Program()
    circ += cnx
    circ += op(0,1,2)
    print(qc.compile(circ))
    return

def transformer_test():
    arc = nx.cycle_graph(4)
    #isa = graph_to_compiler_isa(arc)
    quantum_processor = NxQuantumProcessor(arc)

    qc = _get_qvm_with_topology(name='ring', topology=arc, client_configuration=None, noisy=False,compiler_timeout=600,execution_timeout=600,qvm_type='qvm')



    cnx = DefPermutationGate('CNX', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,14])

    op = cnx.get_constructor()
    circ = Program()
    circ += cnx
    circ += op(0,1,2,3)

    print(qc.compile(circ))

    #ax = plt.plot()
    #nx.draw(arc, with_labels=True, font_weight='bold')
    #plt.show()
    return

def pyquil_ring():
    N = 7
    for i in range(3,N):
        #build quantum computer with topology
        arc = nx.cycle_graph(i)
        qc = _get_qvm_with_topology(name='ring', topology=arc, client_configuration=None, noisy=False,compiler_timeout=600,execution_timeout=600,qvm_type='qvm')
        
        

        #define gate and add gate to cricuit
        op = simple_construct_rev_operation(define_gate_xor(i))
        print(op)
        p = Program().defgate("op", op)
        l = range(i)
        opl = ['op']
        b = [*opl,*l]
        t = tuple(b)
        p.inst(t)

        #print(qc.compile(p))
        with open(str(i)+'xor_ring.txt', 'w') as f:
            f.write(str(qc.compile(p)))
        if i == 6:
            ax = plt.plot()
            nx.draw(arc, with_labels=True, font_weight='bold')
            plt.show()


def pyquil_line():
    N = 7
    for i in range(3,N):
        #define gate and add gate to cricuit
        op = simple_construct_rev_operation(define_gate_or(i))
        
        p = Program().defgate("op", op)
        l = range(i)
        opl = ['op']
        b = [*opl,*l]
        t = tuple(b)
        p.inst(t)

        #build quantum computer with topology
        arc = nx.path_graph(i)
        qc = _get_qvm_with_topology(name='line', topology=arc, client_configuration=None, noisy=False,compiler_timeout=600,execution_timeout=600,qvm_type='qvm')
        
        #print(qc.compile(p))
        with open(str(i)+'or_line.txt', 'w') as f:
            f.write(str(qc.compile(p)))

        if i == 6:
            ax = plt.plot()
            nx.draw(arc, with_labels=True, font_weight='bold')
            plt.show()


#main2()
small_circuits()
#permutation_test()

#transformer_test()

#pyquil_ring()
#pyquil_line()


