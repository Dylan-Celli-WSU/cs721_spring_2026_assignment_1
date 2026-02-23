#!/bin/bash

# run with 'sbatch slurm_launcher.sh'

#SBATCH --job-name=assignment
#SBATCH --time=0-1:00:00   # time
#SBATCH --ntasks=4          # number of processor cores (i.e. tasks)
#SBATCH --nodes=1           # number of nodes
#SBATCH --mem=12G           # set memory to 12 GB per node
#SBATCH --output=Part_A.out

module load Python/3.10.4-GCCcore-11.3.0

# Execute the script
python ./solution.py
