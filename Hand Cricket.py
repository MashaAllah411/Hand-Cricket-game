import random
import time

Name=input("Enter Your Name:").capitalize()
print(f"Hello {Name}, Lets start the game")
time.sleep(2)
Number=[i for i in range(0,7)]
P1=0

condition=True
while condition:
    Computer=random.choice(Number)
    Player1=int(input("Give a Number from 0 to 6:"))
    print(f"Machine Number :{Computer}")
    if Player1>6 :
        print(f"Enter The numbers like(0,1,2,3,4,5,6)")
    print()
    if Computer==Player1:
        print(f"Game Over for {Name}!")
        condition=False
    else:
        P1+=Player1
        time.sleep(1)
    if condition==True:
        if P1>=10 and P1<=20 :
            print(f"Great Start {Name},Your score is {P1}")
            continue
        elif P1>=21 and P1<=30 :
            print(f"Looking good {Name} you are crossed {P1} Runs")
        elif P1>=31 and P1<=49:
            print(f"Just few runs to go!,you are in {P1} Runs")
        elif P1>=50 and P1<=55:
            print(f"Take a Bow for {Name},you are crossed half Century!")
        elif P1>=55:
            print(f"Keep it up!{Name},convert to century")
print()
print(f"{Name} you got the Total Score of:",P1)
print()
print("Now Machine Turn")



C1=0
condition=True
while condition:
    Player1=int(input("Give a Number from 0 to 6:"))
    Computer=random.choice(Number)
    print(f"Machine Number:{Computer}")
    
    print()
    if Player1==Computer:
            print("Game Over for Machine!")
            condition=False
    else:
        C1+=Computer
        time.sleep(1)
    
    
    if condition==True:
        if C1 > P1:
            print("Machine has surpassed your score!")
            break
        elif C1>=10 and C1<=20 :
            print(f"Great Start Machine,Your score is {C1}")
            continue
        elif C1>=21 and C1<=30 :
            print(f"Looking good Machine you are crossed {C1} Runs")
        elif C1>=31 and C1<=49:
            print(f"Just few runs to go!,you are in {C1} Runs")
        elif C1>=50 and C1<=55:
            print(f"Take a Bow for Machine,you are crossed half Century!")
        elif C1>=55:
            print(f"Keep it up!Machine,convert to century")

    

print("Machine Total Score:",C1)
time.sleep(1)

if P1>C1:
    diff=abs(P1-C1)
    print(f"{Name} Won The Match with the difference of {diff}")
else:
    diff2=abs(C1-P1)
    print(f"Machine Won The Match with the difference of {diff2}")

    



