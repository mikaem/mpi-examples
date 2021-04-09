from mpi4py import MPI
comm = MPI.COMM_WORLD
import sys
import numpy as np
import sympy

x = sympy.Symbol("x")
f = eval(sys.argv[-1])

rank = comm.Get_rank()
size = comm.Get_size()
a = 0.0
b = 1.0
N = eval(sys.argv[-2]) # Number of subdivisions for each rank
assert N % 2 == 0

# Mesh decomposition
dx = (b-a)/size
a_hat = rank*dx
b_hat = (rank+1)*dx
xj = np.linspace(a_hat, b_hat, N+1)

# Evaluate function on submesh on each processor
fj = [f.subs(x, y) for y in xj]

# Compute subintegral on each processor
Ij = (b_hat-a_hat)/float(3*N)*((fj[0]+fj[-1])+4*sum(fj[1:-1:2])+2*sum(fj[2:-2:2]))

# Reduce on root (sum all contributions from all ranks)
I = comm.reduce(Ij)

# Compare with exact solution
exact = f.integrate((x, (a, b)))
if rank == 0:
    print("Integral of f(x) from ", a, "to", b, "is", I)
    print("Exact                             = ", exact.evalf())


