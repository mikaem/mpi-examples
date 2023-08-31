from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = None
if rank == 0:
    data = range(comm.Get_size()) # [0, 1, ..., size-1]
    
data = comm.scatter(data, root=0)

print("Rank", rank, "data =", data)
