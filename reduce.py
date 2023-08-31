from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = rank
data = comm.reduce(data, op=MPI.SUM, root=0) # MPI.PROD, MPI.MAX, MPI.MIN

print("On rank", rank,"data =", data)
