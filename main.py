#Function - Determine if current year is leap
def is_leap_year(year):

    return (year % 4 == 0 and year % 100 !=0) or year % 400 == 0

def daysinMonth(month, year):
    
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30
    
#Get Input Month - Check Validation
while True:
    try:
        month = int(input("Enter month number (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print ("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a number.")
#Get Input Year - Check Validation     
while True:
    try:
        year = int(input("Enter year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
 
 #Return Output       
days = daysinMonth(month, year)
print(f"the month {month} in the year {year} has {days} days.")












'''
First attempt - basic logic, no functions.
'''

# is31month = [1,3,5,7,8,10,12]
# is30month = [4,6,9,11]
# is28month = [2]

# x = int(input("Enter a numerical month"))
# determineYear = int(input("Enter year as (XXXX)"))

# if x in is31month: 
#     daysinMonth = "31"
# elif x in is30month:
#     daysinMonth = "30"
# elif x in is28month:
#     determineYear
#     # daysinMonth = "28"
# else :
#     daysinMonth = "Invalid Month"

# if (determineYear % 4) == 0:
#     daysinMonth = 29
    
#     if (determineYear % 100) == 0:
#         daysinMonth = 29
        
#         if (determineYear % 400) == 0:
#             daysinMonth = 29

# else :
#             daysinMonth = 28
        
# print('The number of days in your month is, \n', daysinMonth)

