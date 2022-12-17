import pandas as pd 
import plotly.express as px 
import csv

df1 = pd.read_csv("shared_articles.csv")
df2 = pd.read_csv("users_interactions.csv")

print(df2.head())
print(df1.head())