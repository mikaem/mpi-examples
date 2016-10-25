source ~/.vim/plugin/comments.vima
_world

  ! Include the MPI library definitons:
  include 'mpif.h'

  integer numtasks, rank, ierr, rc, len, i

  ! Initialize the MPI environment
  call MPI_INIT(ierr)

  ! Get the number of processors
  call MPI_COMM_SIZE(MPI_COMM_WORLD, numtasks, ierr)

  ! Get the rank of the process
  call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)

  print "('Hello World! from rank ',I3,' of ',I3,' processors')",&
       rank, numtasks

  ! Finalize the MPI environment
  call MPI_FINALIZE(ierr)

end program hello_world
