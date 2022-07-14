# Get the loan details
money_owed = float(input("How much mondy do you owe, in dolars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your month playment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

monthy_rate = apr/100/12

for i in range(months):

    interest_paid = money_owed * monthy_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payemnt is", money_owed)
        print("you paid off the load in", i+1, "months")
        break

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)