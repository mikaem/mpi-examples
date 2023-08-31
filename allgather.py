from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = rank**2
data = comm.allgather(data)

print("On rank", rank,"data =", data)
    
