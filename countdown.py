#Countdown from user input number that is positive
print('Enter a positive number:')
cDown = int(input())
def countdown(nLines):
    if nLines == 0:
        print('Blastoff!')
    elif nLines <= 0:
        print('Uh Oh!')
    else:
        print(nLines)
        countdown(nLines-1)
countdown(cDown)
