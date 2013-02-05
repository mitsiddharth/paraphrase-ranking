#!/bin/bash

# creates the actual condor file to be submitted


echo 'universe = vanilla'
echo '+Group = "GRAD"'
echo '+Project = "isogram"'
echo '+ProjectDescription = "ukwac"'

for f in `ls -1 /scratch/cluster/sid/ukwac-parsed/*.bz2`
do
  output_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/output/p' | sed -n 's/\.bz2//p'`
  error_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/error/p' | sed -n 's/\.bz2//p'`
  log_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/log/p' | sed -n 's/\.bz2//p'`
  output_folder=$(basename $output_f)
  echo "Executable = /u/sid/paraphrase-ranking/code/collectSentences.sh"
  echo 'arguments = "'4 clever luminous shining promising /scratch/cluster/sid/ukwac-matched-sentences/output/$output_folder $f'"'
  echo "output = $output_f.output"
  echo "log = $log_f.log"
  echo "error = $error_f.error"
  echo "queue"
done
