import csv
# General syntax to import specific functions in a library:
##from (library) import (specific library function)
import pandas as pd
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
#Importer Time

import pandas as pd #this is how I usually import pandas


with open("Feuille1.csv", "r") as firstcsv:
    pass
    #data = firstcsv.read()
    #print(data)
    #data_listed = list(data)

    #print(data_listed)

data = pd.read_csv('Feuille1.csv')
print(data)


