# Criminal-Database-System
Problem Statement:
In this Project we create a database of Criminal record 
according to their Names, Crime, Offense date, 
Disposed Date and Confinement type. Now Write a 
Python Code to Access this data by Different Methods-
• By Display Full List 
• Access the Data by Criminal Name
Create Different Plots using Matplotlib Library in 
Python file.
===>>
Here we Create a Python File and Import the libraries named as 
NumPy, Panda, Matplotlib which we will used in this project.
First, we create a class name Criminal and initialize the variable 
jail as “COUNTY JAIL” and now use _init_ method function to 
assign values to the data members. Now we create another 
function name GetCriminalList using self argument and define a 
dictionary name data in this function where we write the 
database of criminal record such as Names, Charge, Offense Date, 
Disposed Date and Confinement type.
In the end of This function we use Panda Library and use the 
Panda DataFrame to create a data frame using index as the case 
number and pass the dictionary variable data in it and at last use 
print function to print this data base.
---------------------------------------------------------------------------------------
Now use some other functions to print the data Name wise. Here 
we use different functions for different case numbers. In this 
function we store the data of that criminal as name, charge...etc.
And after that we use data frame using pandas with index as the 
case number and pass the criminal details which we store in 
dictionary variable. Similarly create functions for other cases also.
---------------------------------------------------------------------------------------
Now we use if and else for choose the users choice and take input 
of user choice. Now if we run this then it first ask for select choice 
of display the data full list or display the data of a particular 
criminal.
Now if we enter 1 then it shows full list --
Now if we enter 2 then it ask for enter the criminal name and 
then we enter and it provide the full record of that criminal --
Now we create another python file for create some plots related 
to that criminal record database, where we use Matplotlib Library 
in python to create different plots.
In this file we use the same criminal record database and create 
some array using NumPy library in python and use this data of 
array to create plots. When we run this file it will ask user to 
select serial number to which plot you want to see --
Now which plot you want to show enter that number and if you 
enter other than this it will ask to enter a valid number
