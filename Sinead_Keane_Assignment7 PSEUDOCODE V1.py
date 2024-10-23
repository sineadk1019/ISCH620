# -*- coding: utf-8 -*-
"""
Name: Sinead Keane
Class: ISCH 620
Due Date: 12/18/2023
Assignment #7, Pseudo Code
Email: sinead.keane001@gmail.com
"""

#This program will graph, calculate mean/median/mode, standard deviation a particular dataset. 
#This program will also graph the changes in plot given changes in standard deviation. 
#Finally, it will put the values from the dataset into buckets using Pandas. 

Import needed modules

Create an empty list to house our text file numbers.

Try Open and read in values
Check if file exists
      
Begin
    iterate through list to remove non-numerical data
        append list dataset with numerical values for future calculations
        plot values

Define function for standard deviation a manual ostandard deviation
   loop through values and calulcate the variance, total sum of values
   calculate value of standard deviation given the variables above
   print variance and standard deviation formatted
   
Define function for change in standard deviation 
    create standard deviation data set 
    For loop to index and calculate deviation as it moves through the list
    add values to list
    plot values

calculate mean, median, mode as their own variables.
print formatted values of mean, median and mode

Open and read in values using Pandas

Create lists to drop values into

Begin Pandas
    Iterate through list in Pandas
    sort values by buckets
    calculate how many values in each bucket
    append lists
    print totals per bucket