import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt



class Criminal:
    jail="COUNTY JAIL"
    
    def __init__(self,name):
        self.name=name
        # if self.name = "John":
    def GetcriminalList(self):
        data={
            "Name": ['John', 'Ithan','Pekk','Sherlock','Tyrion','Mike',
         'Will','Steve','Dustin','Jonathan','Silverdeev','Majnu Bhai','Selmon Bhoi','Sanjay Dutt'],
            
            "Charge": ['Murder','Kidnapping','Tax Evasion','Blackmail','Child Abuse',
           'Cybercrime','Fraud','Hit and Run','Terrorism','Robbery','Smuggling','Paintings Smuggler','Animal Abuse,Hit and Run',
           'Carrying concealed weapon'],
            
            "Offense Date": ['20/09/2012', '10/01/2015', '11/09/2010','01/01/2020','30/03/2011',
                 '12/12/2015','10/10/2010','09/04/2017','10/03/2005','20/09/2019','20/10/2013','15/09/2013','10/12/2010','15/02/2010'],
            
            "Disposed": ['20/09/2019', '10/01/2019', '11/09/2022','01/01/2023','30/03/2025',
                 '12/12/2022','10/10/2026','09/04/2024','10/03/2029','20/09/2030','20/10/2035','15/03/2024','20/03/2022','12/12/2022'],
            
            "Confinement type": ['COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','COUNTY JAIL',
                     'COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','COUNTY JAIL','TIHAR JAIL','TIHAR JAIL','TIHAR JAIL']
  
        }
        df = pd.DataFrame(data, index = ["case no.1", "case no.2", "case no.3","case no.4","case no.5","case no.6",
                                 "case no.7","case no.8","case no.9","case no.10","case no.11","case no.12","case no.13","case no.14"])
        print(df)    
            
            
            
        
    def case01(self,name):
        data1={
            "Name" : ['John'],
            "Charge":['Murder'],
            "Offense Date":['20/09/2012'],
            "Dispose":['20/09/2019'],
            "Confinement type":['COUNTY JAIL']
        }
        df1 = pd.DataFrame(data1, index = ["case no.1"])
        print(df1)
        
    def case02(self,name):
        data2={
            "Name" : ['Ithan'],
            "Charge":['Kidnapping'],
            "Offense Date":['10/01/2015'],
            "Dispose":['10/01/2019'],
            "Confinement type":['COUNTY JAIL']
        }
        df2 = pd.DataFrame(data2, index = ["case no.2"])
        print(df2) 
        
    def case03(self,name):
        data3={
            "Name" : ['Pekk'],
            "Charge":['Tax Evasion'],
            "Offense Date":['11/09/2010'],
            "Dispose":['11/09/2022'],
            "Confinement type":['COUNTY JAIL']
        }
        df3 = pd.DataFrame(data3, index = ["case no.3"])
        print(df3)
        
    def case04(self,name):
        data4={
            "Name" : ['Sherlok'],
            "Charge":['Blackmail'],
            "Offense Date":['01/01/2020'],
            "Dispose":['01/01/2023'],
            "Confinement type":['COUNTY JAIL']
        }
        df4 = pd.DataFrame(data4, index = ["case no.4"])
        print(df4)
                
    def case05(self,name):
        data5={
            "Name" : ['Tyrion'],
            "Charge":['Child Abuse'],
            "Offense Date":['30/03/2011'],
            "Dispose":['30/03/2025'],
            "Confinement type":['COUNTY JAIL']
        }
        df5 = pd.DataFrame(data5, index = ["case no.5"])
        print(df5)
             
    def case06(self,name):
        data6={
            "Name" : ['Mike'],
            "Charge":['Cybercrime'],
            "Offense Date":['12/12/2015'],
            "Dispose":['12/12/2022'],
            "Confinement type":['COUNTY JAIL']
        }
        df6 = pd.DataFrame(data6, index = ["case no.6"])
        print(df6)
    
    def case07(self,name):
        data7={
            "Name" : ['Will'],
            "Charge":['Fraud'],
            "Offense Date":['10/10/2010'],
            "Dispose":['10/10/2026'],
            "Confinement type":['COUNTY JAIL']
        }
        df7 = pd.DataFrame(data7, index = ["case no.7"])
        print(df7)
             
    def case08(self,name):
        data8={
            "Name" : ['Steve'],
            "Charge":['Hit and Run'],
            "Offense Date":['09/04/2017'],
            "Dispose":['09/04/2024'],
            "Confinement type":['COUNTY JAIL']
        }
        df8 = pd.DataFrame(data8, index = ["case no.8"])
        print(df8)
                
    def case09(self,name):
        data9={
            "Name" : ['Dustin'],
            "Charge":['Terrorism'],
            "Offense Date":['10/03/2005'],
            "Dispose":['10/03/2029'],
            "Confinement type":['COUNTY JAIL']
        }
        df9 = pd.DataFrame(data9, index = ["case no.9"])
        print(df9)
        
    def case10(self,name):
        data10={
            "Name" : ['Jonathan'],
            "Charge":['Robbery'],
            "Offense Date":['20/09/2019'],
            "Dispose":['20/09/2030'],
            "Confinement type":['COUNTY JAIL']
        }
        df10 = pd.DataFrame(data10, index = ["case no.10"])
        print(df10)
        
    def case11(self,name):
        data11={
            "Name" : ['Silverdeev'],
            "Charge":['Smuggling'],
            "Offense Date":['20/10/2013'],
            "Dispose":['20/10/2035'],
            "Confinement type":['COUNTY JAIL']
        }
        df11 = pd.DataFrame(data11, index = ["case no.11"])
        print(df11)  
              
    def case12(self,name):
        data12={
            "Name" : ['Majnu Bhai'],
            "Charge":['Paintings Smuggler'],
            "Offense Date":['15/09/2013'],
            "Dispose":['15/03/2024'],
            "Confinement type":['TIHAR JAIL']
        }
        df12 = pd.DataFrame(data12, index = ["case no.12"])
        print(df12)
        
    def case13(self,name):
        data13={
            "Name" : ['Selmon Bhoi'],
            "Charge":['Animal Abuse,Hit and Run'],
            "Offense Date":['10/12/2010'],
            "Dispose":['20/03/2022'],
            "Confinement type":['TIHAR JAIL']
        }
        df13 = pd.DataFrame(data13, index = ["case no.13"])
        print(df13)
        
    def case14(self,name):
        data14={
            "Name" : ['Sanjay Dutt'],
            "Charge":['Carrying concealed weapon'],
            "Offense Date":['15/02/2010'],
            "Dispose":['12/12/2022'],
            "Confinement type":['TIHAR JAIL']
        }
        df14 = pd.DataFrame(data14, index = ["case no.14"])
        print(df14)    
                    

if __name__ == '__main__':
    dummy = Criminal("dummy1")

    while(True):
        print("Welcome to Criminal Record Database")
        print("1. Display Full list")
        print("2. Display namewise")
        
        user_choice = input()
        if user_choice not in ['1','2']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            dummy.GetcriminalList()

        elif user_choice == 2:
            criminal = input("Enter the name :")
            if criminal=="John":
                dummy.case01(criminal)
                
            elif criminal=="Ithan":
                dummy.case02(criminal)    
                
            elif criminal=="Pekk":
                dummy.case03(criminal)
                
            elif criminal=="Sherlok":
                dummy.case04(criminal)
                
            elif criminal=="Tyrion":
                dummy.case05(criminal)
                
            elif criminal=="Mike":
                dummy.case06(criminal)
                
            elif criminal=="Will":
                dummy.case07(criminal)
                
            elif criminal=="Steve":
                dummy.case08(criminal)
                
            elif criminal=="Dustin":
                dummy.case09(criminal)
                
            elif criminal=="Jonathan":
                dummy.case10(criminal)
                
            elif criminal=="Silverdeev":
                dummy.case11(criminal)
                
            elif criminal=="Majnu Bhai":
                dummy.case12(criminal)
                                                       
            elif criminal=="Selmon Bhoi":
                dummy.case13(criminal)
            
            elif criminal=="Sanjay Dutt":
                dummy.case14(criminal)    

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 not in ['q','c']:
                print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue  






      
                

            
            
        
        
    