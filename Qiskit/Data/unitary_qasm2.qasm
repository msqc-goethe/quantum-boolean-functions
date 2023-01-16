OPENQASM 2.0;
include "qelib1.inc";
gate circuit_165 q0,q1 { u3(pi/2,-pi,-pi/4) q1; cx q0,q1; u3(0,0.46364761,2.677945) q0; u3(pi/2,pi/4,-pi) q1; }
gate circuit_158 q0,q1 { u3(pi/2,-pi,-pi/4) q1; cx q0,q1; u3(0,pi/2,-pi/2) q0; u3(pi/2,3*pi/4,-pi) q1; }
gate circuit_151 q0,q1 { u3(0,2.8023,0.33929261) q0; u3(pi/4,pi/2,0) q1; cx q0,q1; u3(3*pi/4,0,pi/2) q0; u3(pi/3,0.61547971,-2.5261129) q1; cx q0,q1; u3(3*pi/4,0,0) q0; u3(pi/2,-pi/4,0) q1; }
gate circuit_142 q0,q1 { u3(pi/4,-pi/2,0) q0; u3(pi/2,0,-pi) q1; cx q0,q1; u3(3*pi/4,0,pi/2) q0; u3(pi/3,0.61547971,-2.5261129) q1; cx q0,q1; u3(pi,1.4463757,-0.9098188) q0; u3(pi/4,-3*pi/4,-pi/2) q1; }
gate gate_AND p0,p1,p2 {
	circuit_142 p0,p1;
	u(0,0,-pi/4) p2;
	cx p0,p2;
	u(0,0,-pi/4) p2;
	cx p1,p2;
	u(0,0,-pi/4) p2;
	cx p0,p2;
	u(0,0,-pi/4) p2;
	cx p1,p2;
	circuit_151 p0,p1;
	u(pi/2,0,pi) p2;
	cx p0,p2;
	u(pi/2,0,pi) p2;
	u(pi/2,0,pi) p2;
	cx p1,p2;
	u(pi/2,0,pi) p2;
	u(pi/2,0,pi) p2;
	cx p0,p2;
	circuit_158 p0,p1;
	u(pi/2,0,pi) p2;
	u(0,0,-pi/2) p2;
	cx p0,p2;
	cx p1,p2;
	cx p0,p2;
	u(0,0,-pi/2) p2;
	cx p1,p2;
	circuit_165 p0,p1;
}
qreg q[3];
gate_AND q[0],q[1],q[2];
