from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print('On process 0. before sending')
    comm.send(data, dest=1)
    print('On process 0. sended')
elif rank == 1:
    print('On process 1. Before receiving.')
    data = comm.recv(source=0)
    print('On process 1. Received. Data is ',data)