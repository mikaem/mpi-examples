from mpi4py import MPI
import numpy as np
import sys
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()
N = eval(sys.argv[-1])
assert N % size == 0

Np = N//size

# Global matrix A is (N, N). Distribute along first index
# Create a random matrix already distributed
A_local = np.random.random((Np, N))

# Create global x
# Create on rank 0 and broadcast to all ranks
x = np.zeros(N)
if rank == 0:
    x[:] = np.random.random(N)
comm.Bcast(x)

# Compute local contribution to A*x
b_local = np.dot(A_local, x)

# Gather result on all ranks
b = np.zeros(N)
comm.Allgather(b_local, b)

# Now b = A*x on all ranks

# Test accuracy
Ac = np.zeros((N, N))
comm.Allgather(A_local, Ac)
assert np.allclose(np.dot(Ac, x), b)
