OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
rz(pi/32) q[4];
ry(pi/2) q[5];
rx(pi) q[5];
cx q[4],q[5];
rz(-pi/32) q[5];
cx q[4],q[5];
cx q[4],q[3];
rz(-pi/32) q[3];
rz(pi/32) q[5];
cx q[3],q[5];
rz(pi/32) q[5];
cx q[3],q[5];
cx q[4],q[3];
rz(pi/32) q[3];
rz(-pi/32) q[5];
cx q[3],q[5];
rz(-pi/32) q[5];
cx q[3],q[5];
cx q[3],q[2];
rz(-pi/32) q[2];
rz(pi/32) q[5];
cx q[2],q[5];
rz(pi/32) q[5];
cx q[2],q[5];
cx q[4],q[2];
rz(pi/32) q[2];
rz(-pi/32) q[5];
cx q[2],q[5];
rz(-pi/32) q[5];
cx q[2],q[5];
cx q[3],q[2];
rz(-pi/32) q[2];
rz(pi/32) q[5];
cx q[2],q[5];
rz(pi/32) q[5];
cx q[2],q[5];
cx q[4],q[2];
rz(pi/32) q[2];
rz(-pi/32) q[5];
cx q[2],q[5];
rz(-pi/32) q[5];
cx q[2],q[5];
cx q[2],q[1];
rz(-pi/32) q[1];
rz(pi/32) q[5];
cx q[1],q[5];
rz(pi/32) q[5];
cx q[1],q[5];
cx q[4],q[1];
rz(pi/32) q[1];
rz(-pi/32) q[5];
cx q[1],q[5];
rz(-pi/32) q[5];
cx q[1],q[5];
cx q[3],q[1];
rz(-pi/32) q[1];
rz(pi/32) q[5];
cx q[1],q[5];
rz(pi/32) q[5];
cx q[1],q[5];
cx q[4],q[1];
rz(pi/32) q[1];
rz(-pi/32) q[5];
cx q[1],q[5];
rz(-pi/32) q[5];
cx q[1],q[5];
cx q[2],q[1];
rz(-pi/32) q[1];
rz(pi/32) q[5];
cx q[1],q[5];
rz(pi/32) q[5];
cx q[1],q[5];
cx q[4],q[1];
rz(pi/32) q[1];
rz(-pi/32) q[5];
cx q[1],q[5];
rz(-pi/32) q[5];
cx q[1],q[5];
cx q[3],q[1];
rz(-pi/32) q[1];
rz(pi/32) q[5];
cx q[1],q[5];
rz(pi/32) q[5];
cx q[1],q[5];
cx q[4],q[1];
rz(pi/32) q[1];
rz(-pi/32) q[5];
cx q[1],q[5];
rz(-pi/32) q[5];
cx q[1],q[5];
cx q[1],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[3],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[2],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[3],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[1],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[3],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[2],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
cx q[3],q[0];
rz(-pi/32) q[0];
rz(pi/32) q[5];
cx q[0],q[5];
rz(pi/32) q[5];
cx q[0],q[5];
cx q[4],q[0];
rz(pi/32) q[0];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-pi/32) q[5];
cx q[0],q[5];
rz(-3.0434179) q[5];
ry(pi/2) q[5];
