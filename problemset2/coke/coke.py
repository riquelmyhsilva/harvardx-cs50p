def main():

    coke_machine()


def coke_machine(amount_due = 50, change_owed = 0):

    while amount_due > 0:

        coin = int(input("Insert Coin: "))

        if coin == 5:
            amount_due -= 5
            change_owed += 5
        elif coin == 10:
            amount_due -= 10
            change_owed += 10
        elif coin == 25:
            amount_due -= 25
            change_owed += 25
        else:
            None

        if amount_due > 0:
            print("Amount Due:", amount_due)

    if change_owed >= 50:
        change_owed -= 50
        print("Change Owed:", change_owed)


main()
