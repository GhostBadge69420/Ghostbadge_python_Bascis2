birth_year = input('Birth year:')
age = 2022 - int(birth_year)
print(age)

########################################################

birth_year = input('Birth year:')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

########################################################

weight_lbs = input('Weight (lbs):')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = "Game theory for beginners"
print(course)

#########################################################

Course = '''
Hi Canniest,

Here is your first billion dollars to you

Thank you

The NSA

'''

print(Course)

#########################################################

course = 'Game theory for beginners'
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])

#########################################################

course = 'Game theory for beginners'

another = course[:]

print(another)

###########################################################

name = 'Canniest'
print(name[1:-1])