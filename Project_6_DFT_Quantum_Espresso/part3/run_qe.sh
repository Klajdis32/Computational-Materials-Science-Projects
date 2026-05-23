#!/bin/bash
#SBATCH --job-name=qe
#SBATCH --partition=batch
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --output=%j.out
#SBATCH --error=%j.err


module load gcc/9.4.0-eewq4j6  openmpi/4.1.2-nfk6aky quantum-espresso/7.1-jzwixr3

#export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK



srun plotband.x -in plotbands.in > plotbands.out




echo "Run finished with exit code $? at: `date`"