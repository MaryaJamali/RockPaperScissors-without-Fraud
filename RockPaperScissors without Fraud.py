# The random module or "rnd" is actually used to create random selections.
# This random selection can be a number, string, list,....
import random
print("please choose your weapon: ")
print("1. Rock", "2. Paper", "3. Scissor")
while True:
    p_c = int(input("choose 1,2 or 3 and for exit choose 0: "))
    # If the input was 0, it will exit the program. break-->is for loop (for & while)
    if p_c == 0:
        break
    # Sometimes we may want to specify a range of numbers and the output number is in that range,
    # with the difference that I don't want float output anymore.
    # Only in method(random.randint), both sides of the interval are closed,
    # for example: it shows random numbers 1 to 3, not 1 to 2
    m_c = random.randint(1, 3)
    weapons = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
    print("I choose: ", weapons[m_c])
    if p_c == m_c:
        print("Draw")
    elif p_c == 1:
        if m_c == 2:
            print("I won :p ")
        elif m_c == 3:
            print("You won :' ")
    elif p_c == 2:
        if m_c == 3:
            print("I won :p ")
        elif m_c == 1:
            print("You won :' ")
    elif p_c == 3:
        if m_c == 1:
            print("I won :p ")
        elif m_c == 2:
            print("You won :' ")

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
