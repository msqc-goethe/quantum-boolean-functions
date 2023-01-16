from pyquil import get_qc, Program

AND_GATE = [[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0]]

qc = get_qc("3q-qvm",as_qvm=True, compiler_timeout=100)
circuit = Program().defgate('and',  AND_GATE)
circuit.inst(('and',0,1,2))
print(str(qc.compile(circuit)))