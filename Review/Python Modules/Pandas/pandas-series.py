import pandas as pd

# Series are like columns in a table; 1D array
col = [1, 4, 3]

myVar = pd.Series(col)
print("Second val %d:" % myVar[1])  # Access the second element 

# basically creates labels for your index
myVar = pd.Series(col, index=["col1", "col2", "col3"])
print(myVar)
