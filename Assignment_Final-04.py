start_again = True
loop = True
while start_again:
    while loop:
        print("1.The month I selected & the previous month.")
        print("2.Just the month I selected.")
        choices = input("How would you like to see your projection?")
        if choices == "1" or choices == "2":
            amount = int(input("Enter the amount of deposit:"))
            i_r = int(input("Enter the amount of interest rate:"))
            duration = int(input("Enter the duration of the deposits in months:"))
            monthly = []
            for i in range(duration):
                if i > 0:
                    monthly.append(monthly[i - 1] + amount *
                                   (1 + i_r / 1200) ** (i + 1))  # i=1,2,3,4...n
                else:
                    monthly.append(amount * (1 + i_r / 1200) ** (i + 1))  # i =0
                print("The Total Value to Date is:", round(monthly[i], 2))

            table = []
            print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF " + str(amount) +
                  " EVERY MONTH AT AN INTEREST RATE OF " + str(i_r) + "% FOR A PERIOD OF " + str(duration) + " MONTHS")
            for i in range(duration):
                if i > 0:
                    table.append([i + 1, amount, amount * (i + 1), round(monthly[i] - monthly[i - 1] -
                                                                         amount, 2),
                                  round(monthly[i] - amount * (i + 1), 2), round(monthly[i], 2)])
                else:
                    table.append([i + 1, amount, amount * (i + 1), round(monthly[i] - amount, 2),
                                  round(monthly[i] - amount * (i + 1), 2), round(monthly[i], 2)])

            print("{:<8} {:<10} {:<20} {:<25} {:<25} {:<8}".format('Month', 'Deposit', 'Total Deposits',
                                                                   'This Month\'s Interest', 'Total-Intrest Earned',
                                                                   'Total-Value To-Date'))
            if choices == '1':
                for v in table:
                    a, b, c, d, e, f = v
                    print("{:<8} {:<10} {:<20} {:<25} {:<25} {:<8}".format(a, b, c, d, e, f))
            elif choices == '2':  # option 2
                a, b, c, d, e, f = table[duration - 1]
                print("{:<8} {:<10} {:<20} {:<25} {:<25} {:<8}".format(a, b, c, d, e, f))
            print("1. Yes")
            print("2. No")
            start_again = input("Do you want to start again?")
            if start_again == '2':
                start_again = False
                print("Thank you for using our service!")
            while loop:
                if start_again != '1' or start_again != '2':
                    print("Invalid Option. Please Select Option 1 or 2.")
                    loop = False


        else:
            print("Invalid Option. Please Select Option 1 or 2.")