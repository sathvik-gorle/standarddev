import csv
import math
with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
def mean(data):
    n=len(data)
    total=0
    for i in data:
        total +=int(i)
    mean=total/n
    return mean
squaredList=[]
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squaredList.append(a)
sum=0
for i in squaredList:
    sum+=i
result=sum/(len(data)-1)
stdev=math.sqrt(result)
print(stdev)