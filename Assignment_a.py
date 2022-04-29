amount = int(input("Enter the amount of deposit:"))
i_r = int(input("Enter the amount of interest rate:"))
duration = int(input("Enter the duration of the deposits in months:"))
Total_Value_To_Date_01 = (amount*(1+i_r/1200)**duration)
Total_Value_To_Date_02 = amount*((1+i_r/1200)+(1+i_r/1200)**2)
Total_Value_To_Date_03 = amount*((1+i_r/1200)+(1+i_r/1200)**2+(1+i_r/1200)**3)
Total_Value_To_Date_04 = amount*((1+i_r/1200)+(1+i_r/1200)**2+(1+i_r/1200)**3+(1+i_r/1200)**4)
Total_Value_To_Date_05 = amount*((1+i_r/1200)+(1+i_r/1200)**2+(1+i_r/1200)**3+(1+i_r/1200)**4+(1+i_r/1200)**5)
d1 = 1
d2 = 2
d3 = 3
d4 = 4 
d5 = 5
if duration == d1:
    print("The Total Value to Date is:",round (Total_Value_To_Date_01, 2))
if duration == d2:
    print("The Total Value to Date is:",round (Total_Value_To_Date_02, 2))
if duration == d3:
    print("The Total Value to Date is:",round (Total_Value_To_Date_03, 2))
if duration == d4:
    print("The Total Value to Date is:",round (Total_Value_To_Date_04, 2))
if duration == d5:
    print("The Total Value to Date is:",round (Total_Value_To_Date_05, 2))
    
