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
#+ echo=False
#' **Feel free to remove the template code below here and start working on the analysis.** 
print ("Displaying the sample figures")  
#+ echo=False
# create 2D array of table given above 
data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
  
# dataframe created with 
# the above data array 
df = pd.DataFrame(data, columns = ['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'] ) 
  
# create histogram for numeric data 
df.hist() 

# show plot 
plt.show()