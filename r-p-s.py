import random

def play():
    user=input("What is your choice?\n 'r' fro Rock,'s' for Scissers, 'p' for Paper\n")
    computer= random.choice(['r','p','s'])
    print ("The computer chose: {}".format(computer))
    if user==computer:
        return "It's a tie"
    elif (user=='r'and computer=='s') or (user=='s'and computer=='p')\
        or (user=='p'and computer=='r'):
        return "You Won!"
    else:
        return "You lose!"
    
    
print(play())