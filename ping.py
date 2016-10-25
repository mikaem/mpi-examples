from mpi4py import MPI
comm = MPI.COMM_WORLD
assert comm.Get_size() == 2

rank = comm.Get_rank()
sendmessage = "from " + str(rank)

comm.send(sendmessage, dest=(rank+1)%2)
rcvmessage = comm.recv(source=(rank+1)%2)

print "Rank", rank, "received the message '", rcvmessage, "'"