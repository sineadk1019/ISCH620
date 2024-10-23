# -*- coding: utf-8 -*-
"""
Name: Sinead Keane
Class: ISCH 620
Due Date: 12/18/2023
Assignment #7, Full Code
Email: sinead.keane001@gmail.com
"""
#Import the necessary modules.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import statistics as stat

#This is where the data being read in from the file will be stored.
dataset = []

#This reads in the file.
with open("C:\\Users\\sinead.keane\\OneDrive - Intelligent Waves\\Desktop\\Personal\\a7_dataset.txt", "r") as data_file:
   dataset_read = data_file.read()
   # print(dataset_read) #checking the file for errors/white space/what needs to be adjusted for clean data
  
#When the file is read in, it had white space and a linebreak on every line, the next steps remove that    
dataset_organize = dataset_read.split("\n")
for x in dataset_organize:
    if x.strip():
        dataset.append(float(x)) #with the white space and such removed, we append the dataset list with the data transformed as floats.
  
#Calulation for mean, median, and mode.    
mean = sum(dataset)/len(dataset)
median = stat.median(dataset)
mode = stat.mode(dataset)

#Beginning to format the output given the above work. 
print("Welcome to the Final Assignment Plots and Calculations \n")
print(f"This graph read in {len(dataset)} data points. and found the following:\n\
Mean:  {round(mean,2)} \nMedian:  {round(median,2)} \nMode:  {round(mode, 2)} ")

#Manual calculation of the standard deviation.
def std_dev1(dataset):
    dataset_std_list = []
    for x in dataset:
        x = (x-mean)**2
        dataset_std_list.append(x)
    total1 = sum(dataset_std_list)
    variance1 = total1 / len(dataset)
    sqr_root = math.sqrt(variance1)
    print(f"Variance:  {round(variance1)} \nStandard Deviation:  {round(sqr_root, 2)}")
    return sqr_root

#Setting the manual standard deviation function as a callable variable. 
std_dev = std_dev1(dataset)

#Calculating deviations of the mean above and below. 
std_dev1_above = mean + std_dev
std_dev2_above = mean + 2 * std_dev
std_dev3_above = mean + 3 * std_dev
std_dev1_below = mean - std_dev
std_dev2_below = mean - 2 * std_dev
std_dev3_below = mean- 3 * std_dev

#Calculating the empirical rule percentages for output. 
emp_percent1 = np.sum((np.array(dataset) >= std_dev1_below) & (np.array(dataset) <= std_dev1_above)) / len(dataset) * 100
emp_percent2 = np.sum((np.array(dataset) >= std_dev2_below) & (np.array(dataset) <= std_dev2_above)) / len(dataset) * 100
emp_percent3 = np.sum((np.array(dataset) >= std_dev3_below) & (np.array(dataset) <= std_dev3_above)) / len(dataset) * 100

#Percentages of data +- 1/2/3 standard deviations formatted for output. 
print(f"{round(emp_percent1)}% of the data was 1 standard deviation. \n\
{round(emp_percent2)}% was 2 standard deviations. \n\
{round(emp_percent3,1)}% was 3 standard deviations. \n")

#This plots a histogram of the data from dataset.
plt.figure(1)
plt.hist(dataset)
plt.title("Plot 1 - Probability Histogram", fontsize = "x-large")


#This will analyze the change in standard deviation to be used in the second graph.
def graph2_data():
    change_dev = []
    for x in range(1,len(dataset)+1):
        current_dev =  np.std(dataset[:x])
        change_dev.append(current_dev)
    return change_dev

#This makes the function a callable variable for plot 2
second_graph = graph2_data()

#This plots the graph of the change in standard deviation.
plt.figure(2)
plt.plot(second_graph)
plt.title("Plot 2- Standard Deviation Histogram", fontsize = "x-large")

#EXTRA CREDIT:
#This creates buckets for Pandas to sort the data into, calculate total, and display. 
df = pd.read_csv('C:\\Users\\sinead.keane\\OneDrive - Intelligent Waves\\Desktop\\Personal\\a7_dataset.csv')

#create header name
df.columns = ["values"]

#checking column name
#print(df.columns)

# sort into counts of the following groups: -5:0 ; 0:5 ; 5:10 ; 10:15 ; 15:20 ; 20:25
df.sort_values(['values'])

#This splits the dataframe into subsets.
bucket1 = df[(df["values"]>=-5) & (df["values"]<=0)]
bucket2 = df[(df["values"]>=0) & (df["values"]<=5)]
bucket3 = df[(df["values"]>=5) & (df["values"]<=10)]
bucket4 = df[(df["values"]>=10) & (df["values"]<=15)]
bucket5 = df[(df["values"]>=15) & (df["values"]<=20)]
bucket6 = df[(df["values"]>=20) & (df["values"]<=25)]

#Formatted output printed. 
print(f"The following are the values between the given intervals:\n\
-5:0 = {len(bucket1)} \n\
0:5 = {len(bucket2)}\n\
5:10 = {len(bucket3)} \n\
10:15 = {len(bucket4)} \n\
15:20 = {len(bucket5)} \n\
20:25 = {len(bucket6)}")

