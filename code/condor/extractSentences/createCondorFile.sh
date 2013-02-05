#!/bin/bash

# creates the actual condor file to be submitted


echo 'universe = vanilla'
echo '+Group = "GRAD"'
echo '+Project = "isogram"'
echo '+ProjectDescription = "ukwac"'

for f in `ls -1 /scratch/cluster/sid/ukwac-parsed/*.bz2`
do
  output_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-sentences\/output/p' | sed -n 's/\.bz2//p'`
  error_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-sentences\/error/p' | sed -n 's/\.bz2//p'`
  log_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-sentences\/log/p' | sed -n 's/\.bz2//p'`
  echo "Executable = /u/sid/paraphrase-ranking/code/extractSentences.sh"
  echo 'arguments = "'$f'"'
  echo "output = $output_f.output"
  echo "log = $log_f.log"
  echo "error = $error_f.error"
  echo "queue"
done
