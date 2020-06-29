#+ echo=False
# import pandas and matplotlib 
import pandas as pd 
import matplotlib.pyplot as plt 
import time
from anadama2 import PweaveDocument
document = PweaveDocument()

vars = document.get_vars()
#' Date: <%= time.strftime("%m/%d/%Y") %>

#' # Study Title
#' <% print(vars["introduction_text"]) %>


#' # Description
#' This report template. Please follow the following code pattern while doing an analysis. 
#'
#'
#'
#'
#' -----
#+ 
#'
#'
#' **Feel free to remove the template code below here and start working on the analysis.** 
