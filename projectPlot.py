import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Criminal data 
criminal = ('John', 'Ithan','Pekk','Sherlock','Tyrion','Mike',
         'Will','Steve','Dustin','Jonathan','Silverdeev','Majnu Bhai','Selmon Bhoi','Sanjay')
Times = np.array([7,4,12,3,14,7,16,7,24,11,23,11,12,12])
T1 = np.array([0,0,12,0,14,0,16,0,24,11,23,11,12,12])
T2 = np.array([7,4,0,3,0,7,0,7,0,0,0,0,0,0])
year = np.array([2012,2015,2010,2020,2011,2015,2010,2017,2005,2019,2013,2013,2010,2010])

print('Choose the data which you want to see from here -- ')
print('1.For how many years crimnal in jail')
print('2.Criminals for more than 10 years in Jail')
print('3.Criminal for less than 10 years in Jail')
print('4.In which year criminal was caught')
print('Enter the Number of data which you want to see :- ')

x = input()
x=int(x)
if x==1:
  plt.barh(criminal,Times)
  plt.title('punisment timespan of a criminal')
  plt.xlabel('Years of punishment')
  plt.ylabel('Criminal names')
  plt.show()
elif x==2:
  plt.barh(criminal,T1,color='red')
  plt.title('Criminals for more than 10 years in Jail')
  plt.xlabel('Years of punishment')
  plt.ylabel('Criminal names')
  plt.show() 
elif x==3:
  plt.barh(criminal,T2,color='green')
  plt.title('Criminal for less than 10 years i Jail')
  plt.xlabel('Years of punishment')
  plt.ylabel('Criminal names')
  plt.show()  
elif x==4:
  plt.scatter(year,criminal,color='red')
  plt.grid(color='blue',linestyle='--')
  plt.title('In which year criminal was caught')
  plt.xlabel('Offence Year')
  plt.ylabel('Criminal names')
  plt.show()
else:
  print('Please enter a valid choice!!!')  
  
