# import pandas
# make an alias for pandas: pd
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# myvar = pandas.DataFrame(mydataset)
myvar = pd.DataFrame(mydataset)

print(myvar)