#!/usr/bin/env python
# coding: utf-8

# In[2]:


# describing data using statistical methods through implementation of theoretical knowledge
import pandas as pd
import numpy as np
import scipy 
from scipy.stats import skew
from collections import Counter
data =[[10,18,11],[13,15,8],[9,20,3]]
n = len(data)
# Mean for first column with index as 0
length1 = len(data[0])
sum1 = sum(data[0])
mean1 = sum1/length1
# Mean for second column with index as 1
length2=len(data[1])
sum2=sum(data[1])
mean2=sum2/length2
# Mean for third column with index as 2
length3=len(data[2])
sum3=sum(data[2])
mean3=sum3/length3
# Median for first column with index as 0
column1 = data[0]
column1.sort()
# Median for second column with index as 1
column2=data[1]
column2.sort()
# Median for third column with index as 2
column3=data[2]
column3.sort()
median1=column1[length1//2]
median2=column2[length2//2]
median3=column3[length3//2]
# Mode for first column with index as 0
data1 = Counter(column1)
get_mode1 = dict(data1)
mode1=[k for k, v in get_mode1.items() if v==max(list(data1.values()))]
# Mode for second column with index as 1
data2 = Counter(column2)
get_mode2 = dict(data2)
mode2=[k for k, v in get_mode2.items() if v==max(list(data2.values()))]
# Mode for third column with idnex as 2
data3 = Counter(column3)
get_mode3 = dict(data3)
mode3=[k for k, v in get_mode3.items() if v==max(list(data3.values()))]
# Standard Deviation for first column with index as 0 (without python library)
s1 = ((((column1[0]-mean1)**2)+((column1[1]-mean1)**2)+((column1[2]-mean1)**2))/length1)**1/2
# Standard Deviation for first column with index as 0 (with python library)
std1 = np.std(column1)
# Standard Deviation for second column with index as 1 (without python library)
s2 = ((((column2[0]-mean2)**2)+((column2[1]-mean2)**2)+((column2[2]-mean2)**2))/length2)**1/2
# Standard Deviation for second column with index as 1 (with python library)
std2 = np.std(column2)
# Standard Deviation for third column with index as 2 (without python library)
s3 = ((((column3[0]-mean3)**2)+((column3[1]-mean3)**2)+((column3[2]-mean3)**2))/length3)**1/2
# Standard Deviation for thrid column with index as 2 (with python library)
std3 = np.std(column3)
# Range for first column with index as 0
range1=max(column1)-min(column1)
# Range for second column with index as 1
range2=max(column2)-min(column2)
# Range for third column with index as 2
range3=max(column3)-min(column3)
# 25% Percentile for first column with index as 0
a125 = np.array(column1)
p125 = np.percentile(a125,25)
# 30% Percentile for first column with index as 1
a130 = np.array(column1)
p130 = np.percentile(a130,30)
# 75% Percentile for first column with index as 2
a175 = np.array(column1)
p175 = np.percentile(a175,75)
# 25% Percentile for second column with index as 0
a225 = np.array(column2)
p225 = np.percentile(a225,25)
# 30% Percentile for second column with index as 1
a230 = np.array(column2)
p230 = np.percentile(a230,30)
# 75% Percentile for secondcolumn with index as 2
a275 = np.array(column2)
p275 = np.percentile(a275,75)
# 25% Percentile for third column with index as 0
a325 = np.array(column3)
p325 = np.percentile(a325,25)
# 30% Percentile for third column with index as 1
a330 = np.array(column3)
p330 = np.percentile(a330,30)
# 75% Percentile for third column with index as 2
a375 = np.array(column3)
p375 = np.percentile(a375,75)

# Quartile Deviation for first column
qd1 = ((p175)-(p125))/2
# Quartile Deviation for second column
qd2 = ((p275)-(p225))/2
# Quartile Deviation for third column
qd3 = ((p375)-(p325))/2
# Skewness for first column with index as 0
sk1 = skew(column1,axis=0,bias=True)
# Skewness for second column with index as 1
sk2 = skew(column2,axis=0,bias=True)
# Skewness for third column with index as 2
sk3 = skew(column3,axis=0,bias=True)# Kurtosis for first column with index as 0
k1 = scipy.stats.kurtosis(column1, axis=0, fisher=True, bias=True)
# Kurtosis for first column with index as 1
k2 = scipy.stats.kurtosis(column2, axis=0, fisher=True, bias=True)
# Kurtosis for first column with index as 2
k3 = scipy.stats.kurtosis(column3, axis=0, fisher=True, bias=True)
#new data description of the given data
data1 = {"Count":[length1,length2,length3],"Mean":[mean1,mean2,mean3],"Median":[median1,median2,median3],"Mode":[mode1,mode2,mode3],"Range":[range1,range2,range3],"Standard Deviation without Python Libraries":[s1,s2,s3],"Standard Deviation with Python Libraries":[std1,std2,std3],"25%":[p125,p225,p325],"30%":[p130,p230,p330],"75%":[p175,p275,p375],"Quartile Deviation":[qd1,qd2,qd3],"Skewness":[sk1,sk2,sk3],"Kurtosis":[k1,k2,k3]}
dataframe1 = pd.DataFrame(data1)
print(dataframe1)
# References
# 1). https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/
# 2). https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# 3). https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/ (for mean, median and mode)
# 4). https://www.nobledesktop.com/learn/python/range-iqr-percentile-in-python (for range)
# 5). https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy (for percentiles)
# 6). https://www.askpython.com/python/examples/quartile-deviation (for quartile deviation)
# 7). https://www.geeksforgeeks.org/how-to-calculate-skewness-and-kurtosis-in-python/ (for skewness and kurtosis)

