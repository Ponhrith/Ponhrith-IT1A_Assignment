print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF $100.00 EVERY MONTH AT AN INTEREST RATE OF %12.0 FOR A PERIOD OF 5 MONTHS")
table = [[1, 100.00, 100.00, 1.00, 1.00, 101.00],
[2, 100.00, 300.00, 2.01, 3.01, 203.01],
[3, 100.00, 300.00, 3.03, 6.04, 306.04],
[4, 100.00, 400.00, 4.06, 10.10, 410.10],
[5, 100.00, 500.00, 5.10, 15.20, 515.20]]

print("{:<8} {:<10} {:<20} {:<25} {:<8}".format('Month', 'Deposit', 'Total Deposits', 'This Month\'s Interest', 'Total-Intrest Earned', 'Total-Value To-Date'))

for v in table:
  a,b,c,d,e,f = v
  print("{:<8} {:<10} {:<20} {:<25} {:<8}".format(a,b,c,d,e,f))
