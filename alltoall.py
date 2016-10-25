from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = range(comm.Get_size())
data = comm.alltoall(data)

print "On rank", rank,"data =", data
    
