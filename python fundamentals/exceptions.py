age = int(input("Age"))
print(age)

##########################################################################################

# try except

try:
    age = int(input('Age:'))
    print(age)
except ValueError:
    print('Invalid vlaue')

#########################################################################################

# Example

try:
    age = int(input('Age:'))
    income = 20
    risk = income/age
    print(age)
except ValueError:
    print('Invalid value')
 
#####################################################################################

try:
    age = int(input('Age:'))
    income = 20
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid vlaue')

