#!/bin/bash
#always start your commands to eddie using a hash-dollar to start the line
#$ -cwd
#$ -t 1-100
#$ -N ArrayJob
./myanalysisprogram.sh split_reads_directory/reads-$SGE_TASK_ID
#$ -o MyResults.o
#$ -e MyResults.e

#To submit type qsub submission_script.sh

