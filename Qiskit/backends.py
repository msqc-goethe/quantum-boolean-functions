from qiskit import *

IBMQ.load_account()
IBMQ.providers()

provider = IBMQ.get_provider()
print(provider.backends(simulator=False, operational=True))
backendnames = ['ibmq_lima', 'ibmq_belem', 'ibmq_quito', 'ibm_nairobi', 'ibmq_manila', 'ibm_oslo']

for name in backendnames:
    backend = provider.get_backend(name)
    print(backend.configuration().basis_gates)
