from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
message = None
if rank == 0:
    message = "Hi!"

message = comm.bcast(message, root=0)

if rank > 0:
    print("Rank 0 says", message, "to rank", rank)
