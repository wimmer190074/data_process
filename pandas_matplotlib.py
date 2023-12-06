import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./proces_data/01_unemp.csv",sep=",")

print(df)

ds = pd.Series([12, 12, 12], index=['a', 1, 'x'])
