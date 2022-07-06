##=================================================================================================
##=======================Days spent since the beginning of the year================================
##=================================================================================================

##Inputs
Year  =  int(input('Enter the Year: '))
Month =  int(input('Enter the Month: '))
Day   =  int(input('Enter the Day: '))


##-------------------Returning an error if the input value is not correct--------------------------
import sys
if Year <= 0:
    sys.exit("There is no such year!")
    
if Month > 12 or Month <= 0:
    sys.exit("There is no such month!")
    

if Day > 31 or Day <= 0:
    sys.exit("There is no such Day!")
    
    
##----------------------------------a list of month days-------------------------------------------
MonthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

##------calculating the spent days since the begining of the year(Considering the leap years)------
if Year % 400==0 :
    MonthDays[1]=29
    Sum = sum(MonthDays[0:Month-1])+Day
 
elif Year % 4==0 and Year % 100 !=0 :
        MonthDays[1]=29
        Sum = sum(MonthDays[0:Month-1])+Day
        

else:
           MonthDays[1]=28
           Sum = sum(MonthDays[0:Month-1])+Day


print('Date: ', Day , '/' , Month , '/' , Year)
print('Days spent since the beginning of the year:', Sum, 'Days')
