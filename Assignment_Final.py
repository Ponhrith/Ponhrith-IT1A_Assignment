amount = int(input("Enter the amount of deposit:"))
i_r = int(input("Enter the amount of interest rate:"))
duration = int(input("Enter the duration of the deposits in months:"))
#def projection(amount, i_r, duration):
    #month=[]
    #deposit=[]
    #totalDeposit=[]
    #compound=[]
    #for i in range(duration):
        #month.append(i+1)
        #deposit.append(amount)
        #totalDeposit.append(deposit*(i+1))
        #compound.append(deposit*((1*i_r)**(i+1)))
    #totalValueToDate=[]
    #for i in range(duration):
        #totalValueToDate.append(sum(compound[:i+1]))
Total_Value_To_Date_01 = (amount*(1+i_r/1200)**duration)
for x in range(duration):
    