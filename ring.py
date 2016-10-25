from mpi4py import MPI
import sys
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()
sumreceived = 0 
stop = False
recieved = rank
while not stop:
    comm.send(recieved, dest=(rank+1)%size)
    recieved = comm.recv(source=(rank-1)%size)
    sumreceived += recieved
    if recieved == rank: stop = True
    
print "Sum received =", sumreceived




