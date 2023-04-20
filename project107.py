import pandas as pd
import csv 
import plotly.express as px


dataFrames = pd.read_csv("data.csv")
framesInGraph = px.bar(dataFrames, x='Sports', y='Distance(Km)')
framesInGraph.show()

fig.show()