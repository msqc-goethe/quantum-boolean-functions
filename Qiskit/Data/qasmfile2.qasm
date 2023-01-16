OPENQASM 2.0;
include "qelib1.inc";
gate gate_AND q0,q1,q2 { ccx q0,q1,q2; }
qreg q[3];
gate_AND q[0],q[1],q[2];
