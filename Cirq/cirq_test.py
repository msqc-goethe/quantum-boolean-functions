import cirq
import numpy as np

def define_gate(n):
    l = []
    for i in range(2**n):
        l.append(0)
    l[2**n -1] = 1
    #print(l)
    return l

def define_gate_or(n):
    l = []
    for i in range(2**n):
        l.append(1)
    l[0] = 0
    #print(l)
    return l

def create_id(n):
    return np.identity(n*2)

def simple_construct_rev_operation(lookup_table):
    m = create_id(len(lookup_table))
    for i, b in enumerate(lookup_table):
        if b == 1:
            #m.swap_rows(i*2, i*2+1)
            m[[i*2,i*2+1]] = m[[i*2+1,i*2]]
    return m


#print(cirq.optimize_for_target_gateset(circuit, gateset=gateset))


def main():
    N = 7
    for i in range(3,N):
        qubits = cirq.LineQubit.range(i)

        OP = simple_construct_rev_operation(define_gate(i-1))
        and_gate = cirq.MatrixGate(np.array(OP))

        circuit = cirq.Circuit()
        circuit.append(cirq.decompose(and_gate(*qubits)))

        final = cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset())

        print(final)

def small_circuit():
        i = 4
        qubits = cirq.LineQubit.range(i)

        OP = simple_construct_rev_operation([0,0,0,1,0,1,1,1])
        and_gate = cirq.MatrixGate(np.array(OP))
        circuit = cirq.Circuit()
        

        circuit.append(cirq.decompose(and_gate(*qubits)))
        print(circuit)
        
        final = cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset())

        print(final)



def cirq_impl():
    N = 7
    for i in range(3,N):
        
        OP = simple_construct_rev_operation(define_gate(i-1))
        and_gate = cirq.MatrixGate(np.array(OP))

        qubits = cirq.LineQubit.range(i)
        circuit = cirq.Circuit()
        circuit.append(cirq.decompose(and_gate(*qubits)))
  
        final = cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset())
        print(final)

#main()
cirq_impl()
#small_circuit()