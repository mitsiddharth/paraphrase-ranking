#!/bin/bash

# creates the actual condor file to be submitted

echo 'universe = vanilla'
echo '+Group = "GRAD"'
echo '+Project = "isogram"'
echo '+ProjectDescription = "ukwac"'

num_target_words=1
target_words=bright

for target_word in $target_words
do
  args=""
  paraphrases_to_match=`python /u/sid/paraphrase-ranking/code/getParaphrasesList.py 1 $target_word /u/sid/paraphrase-ranking/data/lexsub/trial/gold.trial`
  cnt=0
  for word in $paraphrases_to_match
  do
    cnt=`expr $cnt + 1`
    if [ $cnt -ne 1 ]; then
      echo "Executable = /u/sid/paraphrase-ranking/code/condor/createTextFiles/getText.sh"
      echo 'arguments = "' $word '"'
      echo "error = /scratch/cluster/sid/ukwac-matched-sentences/error/$word.error"
      echo "log = /scratch/cluster/sid/ukwac-matched-sentences/log/$word.log"
      echo "queue"
    fi
  done
done
