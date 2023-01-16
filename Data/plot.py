import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


def plot_AND_fully():
    f, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_AND.ods', engine='odf')
    tket = pd.read_excel('toffoli_test_and.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_AND.ods', engine='odf')

    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    #ax.set_title("log(CX), AND Operator")
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    f.savefig("fully_and.pdf", bbox_inches='tight')

def plot_AND_ring():
    f, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_AND_ring.ods', engine='odf')
    tket = pd.read_excel('ring_architecture.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_AND_ring.ods', engine='odf')

    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    f.savefig("ring_and.pdf", bbox_inches='tight')

def plot_AND_line():
    f, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_AND_Line.ods', engine='odf')
    tket = pd.read_excel('line_architecture_and.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_AND_line.ods', engine='odf')

    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    f.savefig("line_and.pdf", bbox_inches='tight')

def plot_AND_grid():
    f, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_and_square_test.ods', engine='odf')
    tket = pd.read_excel('grid_architecture_and.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_AND_square.ods', engine='odf')

    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    f.savefig("grid_and.pdf", bbox_inches='tight')


def plot_OR():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_Or_gates.ods', engine='odf')
    tket = pd.read_excel('toffoli_test_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_OR.ods', engine='odf')


    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("fully_or.pdf", bbox_inches='tight')
    plt.show()

def plot_OR_ring():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_ring_2.ods', engine='odf')
    tket = pd.read_excel('ring_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_OR_ring.ods', engine='odf')


    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("ring_or.pdf", bbox_inches='tight')
    plt.show()

def plot_OR_line():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_line_2.ods', engine='odf')
    tket = pd.read_excel('line_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_OR_line.ods', engine='odf')


    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("line_or.pdf", bbox_inches='tight')
    plt.show()

def plot_OR_gird():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_grid_2.ods', engine='odf')
    tket = pd.read_excel('grid_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_OR_square.ods', engine='odf')


    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("grid_or.pdf", bbox_inches='tight')
    plt.show()




def plot_XOR():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_XOR.ods', engine='odf')
    tket = pd.read_excel('toffoli_test_xor.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_XOR.ods', engine='odf')
    
    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("fully_xor.pdf", bbox_inches='tight')
    plt.show()

def plot_XOR_line():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_xor_line_2.ods', engine='odf')
    tket = pd.read_excel('line_architecture_xor.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_XOR_line.ods', engine='odf')
    
    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("line_xor.pdf", bbox_inches='tight')
    plt.show()

def plot_XOR_ring():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_xor_ring_2.ods', engine='odf')
    tket = pd.read_excel('ring_architecture_xor.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_XOR_ring.ods', engine='odf')
    
    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("ring_xor.pdf", bbox_inches='tight')
    plt.show()

def plot_XOR_grid():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_xor_square_2.ods', engine='odf')
    tket = pd.read_excel('grid_architecture_xor.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_XOR_square.ods', engine='odf')
    
    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("grid_xor.pdf", bbox_inches='tight')
    plt.show()



#plot_AND_line()
#plot_AND_fully()
#plot_AND_grid()
#plot_AND_ring()

#plot_OR()
#plot_OR_gird()
#plot_OR_line()
#plot_OR_ring()

#plot_XOR()
#plot_XOR_grid()
#plot_XOR_line()
#plot_XOR_ring()


def plot_OR_XY():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_Or_gates.ods', engine='odf')
    tket = pd.read_excel('toffoli_test_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_OR.ods', engine='odf')


    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz'] + pyQuil['xy']), label= 'PyQuil_XY',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()

    fig.savefig("fully_or_xy.pdf", bbox_inches='tight')
    plt.show()


def plot_OR_ring_XY():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_ring_2.ods', engine='odf')
    tket = pd.read_excel('ring_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_OR_ring.ods', engine='odf')


    ax.plot(qiskit['#qubits'],(qiskit['cx']), label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], (tket['cx']), label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz']), label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz'] + pyQuil['xy']), label= 'PyQuil_XY',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("ring_or_XY.pdf", bbox_inches='tight')
    plt.show()

def plot_OR_line_XY():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_line_2.ods', engine='odf')
    tket = pd.read_excel('line_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyquil_OR_line.ods', engine='odf')


    ax.plot(qiskit['#qubits'],(qiskit['cx']), label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], (tket['cx']), label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz']), label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz'] + pyQuil['xy']), label= 'PyQuil_XY',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("line_or_XY.pdf", bbox_inches='tight')
    plt.show()

def plot_OR_gird_XY():
    fig, ax = plt.subplots()
    qiskit= pd.read_excel('qiskit_or_grid_2.ods', engine='odf')
    tket = pd.read_excel('grid_architecture_or.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_OR_square.ods', engine='odf')


    ax.plot(qiskit['#qubits'],(qiskit['cx']), label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], (tket['cx']), label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz']), label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],(pyQuil['cz'] + pyQuil['xy']), label= 'PyQuil_XY',**{'marker': 'o'}, linestyle=':')
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    fig.savefig("grid_or_XY.pdf", bbox_inches='tight')
    plt.show()


plot_OR_XY()
plot_OR_ring_XY()
plot_OR_line_XY()
plot_OR_gird_XY()


def plot_AND_fully_log_test():
    f, ax = plt.subplots()
    qiskit= pd.read_excel('Qiskit_AND.ods', engine='odf')
    tket = pd.read_excel('toffoli_test_and.ods', engine='odf')
    pyQuil = pd.read_excel('pyQuil_AND.ods', engine='odf')

    ax.plot(qiskit['#qubits'],qiskit['cx'], label='Qiskit',**{'marker': 'o'}, linestyle=':')
    ax.plot(tket['#qubits'], tket['cx'], label='T|Ket>',**{'marker': 'o'}, linestyle=':')
    ax.plot(pyQuil['#qubits'],pyQuil['cz'], label= 'PyQuil',**{'marker': 'o'}, linestyle=':')
    #ax.set_title("log(CX), AND Operator")
    ax.set_yscale('log')
    ax.set_ylabel('#CX')
    ax.minorticks_off()
    #ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel('Number of Qubits')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend()
    plt.show()

    f.savefig("fully_and_log.pdf", bbox_inches='tight')

#plot_AND_fully_log_test()