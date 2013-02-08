#!/bin/bash

mkdir /scratch/cluster/sid/ukwac-matched-sentences/text/$1
ls -1 /scratch/cluster/sid/ukwac-matched-sentences/output/*/$1/$1.output | xargs cat > /scratch/cluster/sid/ukwac-matched-sentences/text/$1/$1.text
