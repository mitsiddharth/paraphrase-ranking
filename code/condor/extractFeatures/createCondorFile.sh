#!/bin/bash

# creates the actual condor file to be submitted

echo 'universe = vanilla'
echo '+Group = "GRAD"'
echo '+Project = "isogram"'
echo '+ProjectDescription = "ukwac"'

num_target_words=1
target_word=bright

echo "Executable = /usr/bin/python"
paraphrases_to_match=`python /u/sid/paraphrase-ranking/code/getParaphrasesList.py $num_target_words $target_word /u/sid/paraphrase-ranking/data/lexsub/trial/gold.trial`
echo 'arguments = "' /u/sid/paraphrase-ranking/code/features/collectUnigrams.py $paraphrases_to_match /scratch/cluster/sid/ukwac-matched-sentences/output /scratch/cluster/sid/ukwac-matched-sentences/unigrams/unigrams_'"'
echo "output = /scratch/cluster/sid/ukwac-matched-sentences/unigrams/$target_word.unigrams"
echo "log = /scratch/cluster/sid/ukwac-matched-sentences/log/$target_word.log"
echo "error = /scratch/cluster/sid/ukwac-matched-sentences/error/$target_word.error"

echo "queue"

#for f in `ls -1 /scratch/cluster/sid/ukwac-parsed/*.bz2`
#do
#  output_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/output/p' | sed -n 's/\.bz2//p'`
#  error_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/error/p' | sed -n 's/\.bz2//p'`
#  log_f=`echo $f | sed -n 's/ukwac-parsed/ukwac-matched-sentences\/log/p' | sed -n 's/\.bz2//p'`
#  output_folder=$(basename $output_f)
#  echo "Executable = /u/sid/paraphrase-ranking/code/collectSentences.sh"
#  
#  paraphrases_to_match=`python /u/sid/paraphrase-ranking/code/getParaphrasesList.py $num_target_words $target_word /u/sid/paraphrase-ranking/data/lexsub/trial/gold.trial`
#  echo 'arguments = "' $paraphrases_to_match /scratch/cluster/sid/ukwac-matched-sentences/output/$output_folder $f'"'
#  
#  echo "output = $output_f.output"
#  echo "log = $log_f.log"
#  echo "error = $error_f.error"
#  echo "queue"
#done
