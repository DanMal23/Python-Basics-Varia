
# dataset from: https://paldhous.github.io/ucb/2016/dataviz/datasets.html

import pandas as pd
import numpy as np

df=pd.read_csv('~/Documents/workspaces/Jupyter_u/files/oil_prod.csv')

# T transposes indes and columns
df2=df.T
# saving file

df2.to_csv('~/Documents/workspaces/Jupyter_u/files/oil_prod_t.csv')
dft=pd.read_csv('~/Documents/workspaces/Jupyter_u/files/oil_prod_t.csv',
               index_col = 0, skiprows=1)
dft.to_csv('~/Documents/workspaces/Jupyter_u/files/oil_prod_t2.csv')

dft2=pd.read_csv('~/Documents/workspaces/Jupyter_u/files/oil_prod_t2.csv',
                 index_col = 0)
                 
 # min max value of oil production from 2000-2014
 # def min_max (modified) based on 'Introduction to Data Science in Python' by Coursera
def min_max(row):
    data = row[[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
            2011, 2012, 2013, 2014]]
    return pd.Series({'min': np.min(round(data)), 'max': np.max(round(data))})

dft2.T.apply(min_max, axis=1)                
#output:
'''
 	                        min 	    max
North America 	            15099.0 	21168.0
Central & South America 	6685.0  	8411.0
Europe 	                    3813.0 	    7226.0
Eurasia 	                8185.0 	    13910.0
Middle East 	            21571.0 	27899.0
Africa 	                    7990.0 	    10678.0
Asia & Oceania 	            8250.0 	    9166.0
World 	                    77101.0 	93097.0
'''

# percent growth from 2000-2014                
def percent_growth(row):
    data = row[[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
            2011, 2012, 2013, 2014]]
    return pd.Series({'percent growth': round((np.max(data)*100/np.min(data))-100)})
    
dft2.T.apply(percent_growth, axis=1)
 #output:              
'''
 	                    percent growth
North America 	            40.0
Central & South America 	26.0
Europe 	                    90.0
Eurasia 	                70.0
Middle East 	            29.0
Africa 	                    34.0
Asia & Oceania 	            11.0
World 	                    21.0
'''





