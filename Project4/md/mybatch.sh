#!/bin/bash
#SBATCH -J project4_mc_md
#SBATCH --ntasks=8
#SBATCH --time=01:00:00

module load gcc/9.4.0-eewq4j6 openmpi/4.1.2-nfk6aky lammps/20220623-ly72qgu

echo "Running LAMMPS with $SLURM_NTASKS MPI tasks"

srun lmp -in input.txt > output.txt