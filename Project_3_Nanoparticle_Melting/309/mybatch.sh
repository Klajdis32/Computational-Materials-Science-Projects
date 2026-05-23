#!/bin/bash
#SBATCH -J lammps_melting
#SBATCH --ntasks=8
#SBATCH --time=01:00:00

module load gcc/8.2.0 openmpi/3.1.3 lammps/20180822

echo "Running LAMMPS with $SLURM_NTASKS MPI tasks"

srun lmp -in input.txt > output.txt