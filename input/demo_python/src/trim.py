#!/usr/bin/env python
import pandas as pd
import argparse


def trim_tsv(input,output,lines):
    tsv_read = pd.read_csv(input, sep='\t')
    temp= (tsv_read.head(lines))
    temp.to_csv(output, sep="\t", index=False)
    
parser = argparse.ArgumentParser(description='Read the tsv metadata file')
parser.add_argument('--input', type=str, help='input file')
parser.add_argument('--output', type=str, help='output file')
parser.add_argument('--lines', type=int, help='number of lines')

args = parser.parse_args()
trim_tsv(args.input,args.output,args.lines)