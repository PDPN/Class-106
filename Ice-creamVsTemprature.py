import csv

import plotly.express as px

with open("Ice-Cream.csv"):
     df = csv.DictReader(csv_file)
     fig = px.scatter(df,x="Temprature", y="Ice-Cream", color="week")
fig.show()
