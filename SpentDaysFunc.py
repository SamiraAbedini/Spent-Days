##=================================================================================================         
##=================Days spent since the beginning of the year (Function)===========================
##=================================================================================================

##Defining a function to get the number of spent days since the beginning of the year

def SpentDays(Year , Month , Day):
    "Days spent since the beginning of the year (Function)"
    import sys
    if Year <= 0:
        sys.exit("There is no such year!")

    if Month > 12 or Month <= 0:
        sys.exit("There is no such month!")

    if Day > 31 or Day <= 0:
        sys.exit("There is no such Day!")


    MonthDays = [31,28,31,30,31,30,31,31,30,31,30,31]


    if Year % 400==0 :
        MonthDays[1]=29
        Sum = sum(MonthDays[0:Month-1])+Day

    elif Year % 4==0 and Year % 100 !=0 :
        MonthDays[1]=29
        Sum = sum(MonthDays[0:Month-1])+Day

    else:
        MonthDays[1]=28
        Sum = sum(MonthDays[0:Month-1])+Day

    result = print('Days spent since the beginning of the year:', Sum, 'Days')

    return result
