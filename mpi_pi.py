from mpi4py import MPI
import numpy as np
import sys
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

# Choose number of random data points
N = eval(sys.argv[-1])

# Generate N points (x, y) on each processor 
data = np.random.random((2, N))

# Find radius of each particle
r = np.sqrt(data[0]**2+data[1]**2)

# Count number of particles inside radius
#mycount = len(np.where(r < 1)[0])
mycount = np.count_nonzero(np.where(r < 1, 1, 0))

# Count total number of particles on all processes
totalcount = comm.reduce(mycount, root=0)

# Compute value of PI
if rank == 0:
    PI = 4*float(totalcount) / (N*size)
    print "Pi =", PI
    print "Error =", abs(np.pi-PI)
