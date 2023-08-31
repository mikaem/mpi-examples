from mpi4py import MPI
comm = MPI.COMM_WORLD
assert comm.Get_size() == 2

rank = comm.Get_rank()
count = 0
while count < 5:    
    if rank == count%2:
        count += 1
        comm.send(count, dest=(rank+1)%2)
        print("Rank", rank, "counts", count, "and sends the ball to rank", (rank+1)%2)
        
    elif rank == (count+1)%2:
        count = comm.recv(source=(rank+1)%2)
    comm.barrier()
if rank == 1: print("Rank 1 misses!")