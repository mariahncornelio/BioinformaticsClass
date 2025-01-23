#!/bin/bash
#SBATCH -J OZ199910.1EG         				
#SBATCH -o OZ199910.1EG.o%j
#SBATCH -e OZ199910.1EG.e%j       		
#SBATCH -p RM          								
#SBATCH -N 1               								
#SBATCH -n 128              					
#SBATCH -t 48:00:00        						
#SBATCH --mail-user=mnc3287@mavs.uta.edu	
#SBATCH --mail-type=all    				


### Activate singularity command and enter your earlGrey command line below
### Be sure to specify -t 128 at the end so it uses all 128 cores on the RM node
singularity exec earlgrey.sif earlGrey -g OZ199910.1.fasta -s C_ornata_OZ199910 -o ./OZ199910.1_Outputs -t 128