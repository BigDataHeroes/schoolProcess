#!/bin/bash

source activate keepcodingFinalProject
source properties.sh

python colegiosDataset.py $inputPath $ouPath 
