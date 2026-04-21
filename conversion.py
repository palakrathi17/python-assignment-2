import pandas as pd
a=pd.read_json("employees.json")
a.to_csv("employees.csv",index=False)
print("conversion done!!!!!")