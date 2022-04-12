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
    
print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF $100.00 EVERY MONTH AT AN INTEREST RATE OF %12.0 FOR A PERIOD OF 5 MONTHS")
table = []
if duration == d1:
    table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
elif duration == d2:
    table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
    table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
elif duration == d3:
    table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
    table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
    table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
elif duration == d4:
    table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
    table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
    table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
    table.append([4, 100.00, 400.00, 4.06, 10.10, 410.10])
elif duration == d5:
    table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
    table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
    table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
    table.append([4, 100.00, 400.00, 4.06, 10.10, 410.10])
    table.append([5, 100.00, 500.00, 5.10, 15.20, 515.20])

print("{:<8} {:<10} {:<20} {:<25} {:<8}".format('Month', 'Deposit', 'Total Deposits', 'This Month\'s Interest', 'Total-Intrest Earned', 'Total-Value To-Date'))
for v in table:
    a,b,c,d,e,f = v
    print("{:<8} {:<10} {:<20} {:<25} {:<8}".format(a,b,c,d,e,f))


print("Do you want to start again?")
def options():
    print("1. Yes")
    print("2. No")

loop = True
while loop:
    options()
    choice = input("Please select Option 1 or 2:")

    if choice =='1':
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
        print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF $100.00 EVERY MONTH AT AN INTEREST RATE OF %12.0 FOR A PERIOD OF 5 MONTHS")
        table = []
        if duration == d1:
            table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
        elif duration == d2:
            table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
            table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
        elif duration == d3:
            table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
            table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
            table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
        elif duration == d4:
            table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
            table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
            table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
            table.append([4, 100.00, 400.00, 4.06, 10.10, 410.10])
        elif duration == d5:
            table.append([1, 100.00, 100.00, 1.00, 1.00, 101.00])
            table.append([2, 100.00, 300.00, 2.01, 3.01, 203.01])
            table.append([3, 100.00, 300.00, 3.03, 6.04, 306.04])
            table.append([4, 100.00, 400.00, 4.06, 10.10, 410.10])
            table.append([5, 100.00, 500.00, 5.10, 15.20, 515.20])

        print("{:<8} {:<10} {:<20} {:<25} {:<8}".format('Month', 'Deposit', 'Total Deposits', 'This Month\'s Interest', 'Total-Intrest Earned', 'Total-Value To-Date'))
        for v in table:
            a,b,c,d,e,f = v
            print("{:<8} {:<10} {:<20} {:<25} {:<8}".format(a,b,c,d,e,f))    

        print("Do you want to start again?")
    elif choice =='2':
        print("Thank you for using our service!")
        loop = False
    else:
        print("Invalid Option. Please select Option 1 or 2.")




