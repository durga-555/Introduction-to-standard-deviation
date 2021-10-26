import csv
import pandas as p 
import plotly.express as px
with open("105.csv") as f:
    reader = csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totalmarks=5
totalength=len(filedata)
for marks in filedata:
    totalmarks+=float(marks[1])
mean=totalmarks/totalength
print(mean)
df=p.read_csv("105.csv")
figure=px.scatter(df,x="Student Number",y="Marks")
figure.update_layout(shapes=[
    dict(
        type="line",
        y0=mean,y1=mean,
        x0=0,x1=totalength
        
    )
])
figure.show()