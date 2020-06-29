#!/usr/bin/env python
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import time
import argparse


def plot_tsv(input, output_dir):
    data= pd.read_csv(input, sep='\t')
    df = pd.DataFrame(data, columns = ['sample', 
                                        'Archaea|Euryarchaeota|Methanobacteria|Methanobacteriales|Methanobacteriaceae|Methanobrevibacter'])
    # create histogram for numeric data 
    df.hist() 
    plt.savefig(output_dir+'/barplots.png')
    
    np.random.seed(1234)
    df_box = pd.DataFrame(np.random.randn(50, 2))
    df_box['g'] = np.random.choice(['A', 'B'], size=50)
    df_box.loc[df_box['g'] == 'B', 1] += 3
    bp = df_box.boxplot(by='g')
    plt.savefig(output_dir+'/boxplots.png')
    
parser = argparse.ArgumentParser(description='Read the tsv metadata file')
parser.add_argument('--input', type=str, help='input file')
parser.add_argument('--output', type=str, help='output file')

args = parser.parse_args()
plot_tsv(args.input, args.output)
