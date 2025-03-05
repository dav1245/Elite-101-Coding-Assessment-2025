restaurant = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

#Level 1
print ("Let's find you a table.")
#Quick message to begin the program

column = [1, 2, 3, 4, 5, 6]

[choice1] =  input ("Choose a number from 1 to 6. This will be the row: ")
#allows the user to choose which row they want

occupied = 'o'

for occupied in restaurant[int(choice1)][int(float(int(column)))] in restaurant:
    print (column)


#output = str(restaurant([str(int(choice1))], []))
#used the get function in order to specify the row AND column

#for occupied in restaurant:
    #clarifies that its looking for OCCUPIED tables
#    print(output)
#should print the row and column

#----------------------------------------------------------------------------------------

#Level 2
party_size1 = input ("How many people are you bringing?")

for occupied in column in restaurant[int(choice1)][int(float(int(column)))]:
    if party_size1 <= occupied in column:
        print (column)

#----------------------------------------------------------------------------------------

#Level 3
party_size2 = input ("How many people are you bringing?")

for occupied in all: column in restaurant
if party_size2 <= occupied in all: column
print (all, column)

#----------------------------------------------------------------------------------------

#Level 4

#Plan: #Take input, make a for loop with restarant[row][input] in restaraunt
#For all occupied in restaurant (list), if occupied is in [row]
#if number of occupied in multiple columns >= input
#print all columns
