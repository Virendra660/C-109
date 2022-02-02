import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)

mean=sum(diceresult)/len(diceresult)
standarddeviation=statistics.stdev(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)
print("Mean is ",str(mean))
print("Median is ",str(median))
print("Mode is ",str(mode))