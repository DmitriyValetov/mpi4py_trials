1) install mpi
2) use: $ mpiexec -n 4 python script.py

sometimes use mpirun instead of mpiexec

https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html

MPI - message passing interface

В первую очередь MPI ориентирован на системы с распределенной памятью, то есть когда затраты на передачу данных велики, в то время как OpenMP ориентирован на системы с общей памятью (многоядерные с общим кешем). Обе технологии могут использоваться совместно, чтобы оптимально использовать в кластере многоядерные системы. 