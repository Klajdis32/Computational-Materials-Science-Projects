#!/bin/bash
#SBATCH -J test
#SBATCH --ntasks-per-node=1     # Number of CPUs
#SBATCH --nodes=1               # Number of nodes
#SBATCH --time=00:15:00         # hh:mm:ss

# module avail
module load gcc/8.2.0  openmpi/3.1.3  lammps/20180822

echo "Running lammps with" $SLURM_NPROCS "MPI tasks"

srun lmp < input.txt > output.txt