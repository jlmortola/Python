#this code will return your age in days
#you need to give the function total_days your birthday & current day. Ex:
#total_days(1984,12,1,2016,10,27)


#daysNdays helper checks if the first date is earlier than the 2nd 
def daysNdays (year1, month1, day1, year2, month2, day2):
    if (year1 < year2):
        return True
    if (year1 == year2):
        if(month1 < month2):
            return True
        if(month1 == month2):
            return day1 < day2
    else:
        return False

#day_after helper calculates the number of days between the dates you give
def day_after (year, month, day):
    if day < leap_year(year, month, day):
        return (year, month, day+1)
    elif (day == leap_year(year, month, day)) and (month < 12):
        return (year, month +1, 1)
    elif month == 12:
        return (year + 1, 1, 1)

#leap_year helper finds how many leap years have been since you were born
def leap_year (year, month, day):
    if month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if year % 4 == 0 and (year %100 != 0 or year %400 == 0):
            return 29
        else:
            return 28

#total_days main function to calculate your age
def total_days(year1, month1, day1, year2, month2, day2):
    count = 0
    while daysNdays (year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = day_after (year1, month1, day1)
        count += 1
    return count

print total_days(1984,12,1,2016,10,27)
