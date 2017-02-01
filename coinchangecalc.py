
#this code will return which and how many coins you should give to a costumer

def change(money):
    reminder = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    money = round(money * 100)
    #the functions uses the modulo op to detect the reminder
    #reminder is used to find out what coins we should use
    quarter = int(money / 25)
    reminder = money % 25
    dime = int(reminder / 10)
    reminder %= 10
    nickel = int(reminder / 5)
    reminder %= 5
    penny = int(reminder / 1)

    return "quarters: " + str(quarter) +", dimes: " + str(dime) + ", nickels: " + str(nickel) + ", pennys: " + str(penny)


print change(4.20)
