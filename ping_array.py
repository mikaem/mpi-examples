from mpi4py import MPI
comm = MPI.COMM_WORLD
assert comm.Get_size() == 2
import numpy as np
import sys

rank = comm.Get_rank()
N = eval(sys.argv[-1])
sendarray = np.random.random(N)  # Create N random floats
recvarray = np.zeros(N)
comm.Send(sendarray, dest=(rank+1)%2)
comm.Recv(recvarray, source=(rank+1)%2)

print "Rank", rank, "sent the array    ", sendarray
print "Rank", rank, "received the array", recvarray