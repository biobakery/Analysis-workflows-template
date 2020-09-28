#!/usr/bin/env Rscript
require(docopt)
'Usage:
   demo_models.R [-d <sample metadata> -o <output>]

Options:
   -d sample metadata
   -o model output [default: results.csv]

 ]' -> doc

opts <- docopt(doc)

library(tidyverse)
library(reshape2)

# microbiome data

microbiome_melt <- read.csv(opts$d, sep="\t", header=T) %>%
	mutate(sample_id = factor(sample_id)) %>%
	melt() %>%
	dplyr::filter(value > 0)

eps <- min(microbiome_melt$value)

write.table(eps, opts$o, sep="\t", quote=F, row.names=F)