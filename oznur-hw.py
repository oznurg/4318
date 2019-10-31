import pandas as pd
import os

filename = os.getcwd() + "/dataset.csv"
print(filename)
df = pd.read_csv(filename)

sum_df = df.groupby(['Company','Payment'])['Quantity'].sum().unstack()


print(sum_df)


for index, row in sum_df.iterrows():
    print("From", index, row["Cash"], "people have bought stuff on discount and paid in cash, also assistants got", row["Credit"], "servings of coffee on credit.")
    
    
    

#unstack dataframe çevirmek için
#çevirince company nameleri index olarak tuttu
