import random
import sys

def split(f, b, l): #Takes the friends dictionary, the bill, and the lucky flag
        num = f.__len__()
        if l:
            num -= 1
        split = round((b / num), 2)
        for each in f:
            f[each] = split
        return f

def luckyOne(l):            #Takes a dictionary as an argument
    g = list(l.keys())      #Creat a list of the keys
    w = random.choice(g)    #Pick one
    return(w)               #...and return it.

if __name__ == '__main__':

    try:
        friend_count = int(input('Enter the number of friends joining (including you): '))
    except ValueError:
        friend_count = 0 #Well, if that's how you're going to be...
    if friend_count > 0:
        friends = {}
        for each in range(friend_count):
            friend = input('Enter the name of every friend (including you), each on a new line: ')
            friends[friend] = 0
        bill = int(input('Enter the total bill value: '))
    else:
        print('No one is joining for the party')
        sys.exit(0)

    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if lucky == 'Yes':
        lucky = True
        winner = luckyOne(friends)
        print(f'{winner} is the lucky one!')
    else:
        lucky = False
        print('No one is going to be lucky')
    friends = split(friends, bill, lucky)
    if lucky: #lucky is now a boolean...
        friends[winner] = 0.00
    print(friends)