#!/bin/bash

ARGS=("$@")
num_words=$1
python_args=$num_words
echo "num_words = $num_words"

output_path=${ARGS[$(($num_words + 1))]}
echo "output_path = $output_path"

for i in `seq 1 $num_words`
do
  mkdir $output_path
  mkdir $output_path/${ARGS[$i]}
done

segment_path=${ARGS[$((num_words + 2))]}
echo "segment_path = $segment_path"

bzcat $segment_path | grep "^<c>" | sed -n 's/^<c> \(.*\)/\1/p' | python /u/sid/paraphrase-ranking/code/collectSentences.py $@
