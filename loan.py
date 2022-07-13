# Get the loan details
money_owned = float(input("How much money do you owe, in dollars? \n")) #30,000
apr = float(input("What is the annual percentage rate?\n")) #3%
payment = float(input("Payment in dollars?\n")) #400
months = int(input('Want to see results?'))

#divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # to indent a block of code ctrl + ]

    # Add in interest 
    interest_paid = money_owned * monthly_rate
    monthly_rate = money_owned + interest_paid

    if (money_owned - payment < 0):
        print ("The last payemnt,", money_owned)
        print("You paid off the load in",i+1, "months")
        #break statment to get out of loop
        break

    # make payment 
    money_owned = money_owned - payment 

    # Print the results after this month 
    print("Paid", payment, "of which", interest_paid, "was interest")
    print("Now I owe", money_owned)
